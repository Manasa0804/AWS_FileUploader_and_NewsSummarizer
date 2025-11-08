# **Challenge 2: AWS Lambda News Summarizer**

### **Objective**

A serverless AWS Lambda function that takes a news article URL as input and returns a short summarized version using the Hugging Face NLP API.

---

### **Setup Instructions**

1. Installed dependencies locally for packaging:

   ```bash
   pip install requests beautifulsoup4 -t .
   ```

2. Placed `lambda_function.py` inside the same folder and zipped all files:

   ```bash
   zip -r summarizer.zip .
   ```

3. Created AWS Lambda function

   - Runtime: Python 3.9
   - Uploaded `summarizer.zip` under Code Source

4. Added environment variable:

   ```
   - Key: HF_API_TOKEN
   - Value: your_hugging_face_token_here
   ```

5. Added API Gateway trigger:

   - Trigger → API Gateway → HTTP API → Open Access
   - Copied the Invoke URL for testing

7. Tested the function using a sample event:

   ```json
   {
     "body": "{\"url\": \"https://www.npr.org/2024/02/15/ai-chatbots-work-productivity-study\"}"
   }
   ```

8. Verified output in Lambda → Test Results:

   ```json
   {
     "summary": "A recent study found that AI chatbots can improve work productivity but may reduce creativity."
   }
   ```
9. Tested the Flask app locally by running:

  - python app.py
    
10.Final Result:A fully functional serverless news summarizer that extracts and summarizes online articles using AWS Lambda and Hugging Face NLP.

---




