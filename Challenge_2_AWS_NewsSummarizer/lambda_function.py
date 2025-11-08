import json
import os
import requests
from bs4 import BeautifulSoup

# Hugging Face API
HF_API_URL = "https://router.huggingface.co/hf-inference/models/sshleifer/distilbart-cnn-12-6"

HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
if not HF_API_TOKEN:
    HF_API_TOKEN = "hf_xxxxxxxxxxxx"


def extract_text(url):
    """Extracts readable text from a news article using requests + BeautifulSoup."""
    response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")

    # Try multiple patterns to grab text content
    selectors = ["article p", "div p", "section p", "p"]
    paragraphs = []
    for selector in selectors:
        found = soup.select(selector)
        if found:
            paragraphs = found
            break

    text = " ".join(p.get_text() for p in paragraphs)
    return text.strip()[:3000]  # limit text length

def summarize_text(text):
    headers = {"Authorization": f"Bearer {HF_API_TOKEN}"}
    payload = {"inputs": text[:1000]}  # limit input text length
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    try:
        result = response.json()
        print("HF API Response:", result)

        # If model is loading, handle it
        if isinstance(result, dict) and "error" in result:
            return f"Hugging Face API Error: {result['error']}"

        # If summary is returned properly
        if isinstance(result, list) and "summary_text" in result[0]:
            return result[0]["summary_text"]

        return "Unexpected response format from Hugging Face API."

    except Exception as e:
        return f"Error parsing Hugging Face response: {str(e)}"


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        url = body.get("url")

        if not url:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing 'url'"})}

        article_text = extract_text(url)
        if not article_text:
            return {"statusCode": 400, "body": json.dumps({"error": "No text found in the article"})}

        summary = summarize_text(article_text)
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"summary": summary})
        }

    except Exception as e:

        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
if __name__ == "__main__":
    # For local testing only
    test_event = {
        "body": json.dumps({
            "url": "https://www.npr.org/2024/02/15/ai-chatbots-work-productivity-study"
        })
    }

    result = lambda_handler(test_event, None)

    print("\nStatus Code:", result["statusCode"])
    print("Summary:\n")

    # Parse the summary JSON and print clearly
    try:
        body = json.loads(result["body"])
        print(body["summary"])
    except Exception as e:
        print("Error reading summary:", e)
        print(result)

