# Markdown-to-HTML

## What the app does (concise)
This web application allows users to upload .md (Markdown) files, converts them to HTML, and caches the result using Redis. The conversion ensures faster access for the same file reducing server load.

## How the app functions (concise)
It imports necessary libraries like os, redis, and Flask. Then, it sets up a Flask application and enables Redis caching to improve performance. It defines allowed file extensions (only .md files). So it accepts only markdown files and saves them ssecurely. There's an allowed_file function that checks if the file extension is allowed. The app has an /upload endpoint that supports the POST method. If no file or an empty file is uploaded, it returns a 400 error. If the file is valid, it checks for cached HTML content in Redis; if not found, it converts the Markdown to HTML using the convert_md_to_html function.

# Proper explanation of code

1. Importing Required Modules
os: Used for interacting with the operating system, like handling file paths and directories.
redis: Provides a client to interact with a Redis database for caching.

## Flask and related modules;
Flask: The web framework
request: To access incoming request data
jsonify: To send JSON responses
werkzeug.utils.secure_filename: Ensures that the filenames are safe to use
convert_md_to_html from converter: A custom function (defined in converter.py) that converts Markdown content to HTML

![image](https://github.com/user-attachments/assets/bda28020-c99f-42c5-8235-4c422ff61bd7)


2. Initializing the Flask App and Configuring Redis

![image](https://github.com/user-attachments/assets/8be2bdb7-3bfd-4bdb-bbcc-a42029377cbc)

It creates an instance of flask web application, then it connects to a Redis server running locally on the default port. The parameter decode_responses=True ensures that responses from Redis are returned as strings instead of bytes.


3. Configuring file uploads

Here I'm are restricting the uploads to markdown files only. Then created an uploads directory and and configured app such that it stores files uploaded by the user in it. I also defined a function that checks if uploaded files have .md type extension.

![image](https://github.com/user-attachments/assets/e6b43427-6017-4fd0-a717-3f9a416a1f9a)


4. API endpoint and file handling

![image](https://github.com/user-attachments/assets/39431666-1081-42d2-be5a-6df078338dc6)

This line defines endpoint at /upload, so when a client (like a web browser or another service) sends an HTTP POST request to http://<your-server>/upload, the server causes the upload_file function to run.


![image](https://github.com/user-attachments/assets/039c64b7-fcd6-4f81-b818-9f158b65ec82)

The first if statement checks if the file is included in the data or not, then it assign the file to the variable named file. The second if statement checks if the file has a name, else it returns an error.


5. File saving, caching using redis, convertion using custom function

![image](https://github.com/user-attachments/assets/4207a1b4-a8a9-4441-8284-139aaa532177)

First it checks if file exists and has allowed extension (.md in this case). Then it secures the file and saves it in uploads folder. It sanitizes file name using secure_filename(file.filename) that is imported from werkzeug.utils.


![image](https://github.com/user-attachments/assets/ffd69b9b-fa17-4b52-992e-8b9ca676f544)

Before processing, the code checks if the HTML conversion for this file is already cached in Redis. If it is, it returns the cached HTML directly.


![image](https://github.com/user-attachments/assets/0686fee8-6183-4c88-8455-ab7359e079aa)

It uses the custom function to convert markdown content into html.


![image](https://github.com/user-attachments/assets/80ac7487-a32e-48d9-81e1-3c7b138852e1)

After conversion, the result is stored in redis for a time period that I can set.
The HTML content is then returned as JSON response.











