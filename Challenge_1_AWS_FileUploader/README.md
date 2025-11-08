# AWS File Uploader (Flask + S3)

### Objective
A simple Flask web app to upload files directly to AWS S3 and return a public URL.

### Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure AWS credentials using `aws configure` or environment variables.
3. Update `S3_BUCKET` and `S3_REGION` in `app.py`.
4. Run the app:
   ```bash
   python app.py
   ```
5. Visit `http://127.0.0.1:5000/` to upload files.

### AWS Requirements
- Create an S3 bucket and make it public.
- Ensure CORS and permissions are properly configured.

### Bonus Ideas
- Add file type/size restrictions
- Store metadata in DynamoDB
- Deploy using Render or AWS Elastic Beanstalk
