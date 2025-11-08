# Challenge 1: AWS File Uploader (Flask + S3)

### Objective
A simple Flask web app to upload files directly to AWS S3 and return a public URL.

### Setup Instructions
1.Created a Flask project with the following structure:

   ```
   app.py
   templates/
     └── index.html
   requirements.txt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure AWS credentials using `aws configure` or environment variables.
4. Update `S3_BUCKET` and `S3_REGION` in `app.py`.
5. Run the app:
   ```bash
   python app.py
   ```
6. Visit `http://127.0.0.1:5000/` to upload files.
7. Uploaded a test file (`test.txt`), verified it appeared in S3, and got a public file URL.
8. Final Result:A working Flask app that uploads files directly to an AWS S3 bucket and returns a public download link.


