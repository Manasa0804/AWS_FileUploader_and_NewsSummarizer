## Hosted Live Demos

### Challenge 1 — AWS File Uploader
- Render URL: [https://aws-file-uploader-rgza.onrender.com](https://aws-file-uploader-rgza.onrender.com)
- Description: Uploads files to AWS S3 and returns a public download URL.

### Challenge 2 — AWS News Summarizer
- API Gateway Endpoint: [https://w98n4it5ia.execute-api.ap-southeast-2.amazonaws.com/default/newsSummarizer](https://w98n4it5ia.execute-api.ap-southeast-2.amazonaws.com/default/newsSummarizer)
- Description: Takes a news URL and returns a summarized version using Hugging Face API.

## Short Reflection

Through these tasks, I learned how to integrate AWS services such as S3 and Lambda with Python applications.
The tricky part was managing dependencies and Hugging Face’s API updates, especially the new inference endpoint.
I also gained confidence using environment variables for secure token handling and deploying serverless functions.


## AI Tool Usage Explanation

I used ChatGPT to assist with generating and refining the Python code for both projects:

For Challenge 1 (AWS File Uploader), I used AI guidance to structure the Flask app, integrate it with AWS S3 using boto3, and understand how to configure IAM permissions and public access for uploaded files. The AI helped simplify AWS setup steps and resolve issues like missing credentials or CORS permissions.

For Challenge 2 (AWS News Summarizer), I used AI assistance to write the Lambda function logic, fix import errors (_imaging issue), optimize dependencies by switching from newspaper3k to BeautifulSoup, and update the Hugging Face API endpoint to the latest router version. The AI also helped with generating curl commands and testing steps for API Gateway integration.

After using AI-generated suggestions as a base, I manually tested, debugged, and deployed both applications successfully on AWS.
