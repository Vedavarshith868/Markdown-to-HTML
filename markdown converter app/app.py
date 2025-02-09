#app.py (how api should work)

import os
import redis
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from converter import convert_md_to_html

#initialize Flask app
app = Flask(__name__)

#setting up Redis connection
##redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)
REDIS_URL = os.getenv("REDIS_URL", "redis://default:ATGmAAIjcDFhOTcxYzEyMjg1NTI0ZjdjYjI0NjZlMzM3NTZlNDdiNXAxMA@talented-fawn-12710.upstash.io:6379")
redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

#allowing only those files whose extension type is md
ALLOWED_EXTENSIONS = {'md'}

#creating uploads directory for storing uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#function that checks if uploaded file has allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#API to upload markdown file and convert it to HTML
@app.route('/upload', methods=['POST']) #endpoint is /upload, method type is post
def upload_file():   
    
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        #securing and saving
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        #checking if HTML result is cached in Redis (optional work)
        if redis_client.exists(filename):
            return jsonify({'html': redis_client.get(filename)}), 200

        #reads the file content and convert to HTML
        with open(file_path, 'r') as f:
            md_content = f.read()
        html_content = convert_md_to_html(md_content)

        #cache the HTML result in Redis for future requests
        redis_client.setex(filename, 3600, html_content)  #cache for 1 hour, can variably set time

        #return the HTML result
        return jsonify({'html': html_content}), 200

    return jsonify({'message': 'Invalid file format. Please upload a .md file.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
