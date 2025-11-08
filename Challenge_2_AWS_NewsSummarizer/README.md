# AWS Lambda News Summarizer

### Objective
Create a serverless function that takes a news article URL as input and returns a short summarized version using a free NLP API (Hugging Face).

### Setup Steps

1. **Install dependencies locally (for packaging):**
   ```bash
   pip install requests newspaper3k -t .
   ```

2. **Place this file (`lambda_function.py`) inside the same folder and zip everything:**
   ```bash
   zip -r news_summarizer.zip .
   ```

3. **Deploy to AWS Lambda:**
   - Go to AWS Console → Lambda → Create function (Python 3.9).
   - Upload `news_summarizer.zip` under *Code source*.
   - Add environment variable:
     - Key: `HF_API_TOKEN`
     - Value: `your_hugging_face_token_here`

4. **Add API Gateway Trigger:**
   - Add Trigger → API Gateway → HTTP API → Open.
   - Copy the Invoke URL to test.

5. **Test with curl or Postman:**
   ```bash
   curl -X POST https://your-api-url.amazonaws.com/default/newsSummarizer    -H "Content-Type: application/json"    -d '{"url": "https://www.bbc.com/news/technology-70012345"}'
   ```

### Output Example
```json
{
  "summary": "BBC reports that new AI regulations are being discussed globally..."
}
```

### Behind the Scenes
- AWS Lambda receives the POST request from API Gateway.
- The `newspaper3k` library extracts article text.
- The Hugging Face API generates a concise summary.
- Lambda returns the result in JSON format.
