# Challenge 2 : AWS Lambda News Summarizer

### Objective

Create a serverless AWS Lambda function that takes a news article URL as input and returns a short summarized version using the Hugging Face NLP API.

### Setup Steps

1.Install dependencies locally (for packaging):

pip install requests beautifulsoup4 -t .


2.Place this file (lambda_function.py) inside the same folder and zip everything:

zip -r summarizer.zip .

3.Deploy to AWS Lambda:

Go to AWS Console → Lambda → Create function (Python 3.9)

4.Choose Author from scratch

Upload your news_summarizer.zip file under Code Source

5.Add Environment Variable:

Key: HF_API_TOKEN
Value: your_hugging_face_token_here

6.Add API Gateway Trigger:

Go to Lambda → Add Trigger → API Gateway

Choose HTTP API and set it to Open

Copy the Invoke URL shown after creation

7.Tested the Flask app locally by running:

python app.py
