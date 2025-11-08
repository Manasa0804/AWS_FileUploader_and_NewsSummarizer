from flask import Flask, request, render_template
import boto3
from werkzeug.utils import secure_filename

app = Flask(__name__)

S3_BUCKET = "prgs-demo-bucket"
S3_REGION = "ap-southeast-2"

s3 = boto3.client("s3", region_name=S3_REGION)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file selected", 400

    filename = secure_filename(file.filename)

    s3.upload_fileobj(
        file,
        S3_BUCKET,
        filename,
        ExtraArgs={
            'ContentType': file.content_type,
            'ACL': 'public-read',
            'ContentDisposition': 'inline'   
        }
    )

    file_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{filename}"
    return f"Uploaded! <a href='{file_url}' target='_blank'>{file_url}</a>"

if __name__ == '__main__':
    app.run(debug=True)
    
