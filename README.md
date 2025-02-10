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

It creates an instance of flask web application, then it connects to a Redis server running locally on the default port. The parameter decode_responses=True ensures that responses from Redis database are returned as strings instead of bytes.


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

Before processing, the code checks if the HTML conversion for this file is already cached in Redis database. If it is, it returns the cached HTML directly.


![image](https://github.com/user-attachments/assets/0686fee8-6183-4c88-8455-ab7359e079aa)

It uses the custom function to convert markdown content into html.


![image](https://github.com/user-attachments/assets/80ac7487-a32e-48d9-81e1-3c7b138852e1)

After conversion, the result is stored in redis database for a time period that I can set.
The HTML content is then returned as JSON response.




# Creating a basic web application (not a part of task, I wanted to do it)
This code is a web-based application built with Streamlit. It allows users to upload a markdown file, which is then sent to a local server for conversion into HTML. The app displays both the original markdown code and the generated HTML preview side by side.


![image](https://github.com/user-attachments/assets/78ba805b-1dd4-4b51-b4f7-be74d08d32e9)

I imported the necessary libraries streamlit and requests, of which streamlit is used to build web applications in python and requests simplifies making HTTP requests.


![image](https://github.com/user-attachments/assets/16ec1424-62d5-4320-8db3-618ac809e0fe)

st.set_page_config(...) -> this function sets up configuratyion for Streamlit app.
Here we set the title of the browser and configure the layout to use the full width of page useful for displaying both the contents side-by-side.

st.title(...) -> displays large header at the top of the app.
st.markdown(...) -> Gives short description of the title and instructs user to upload a markdown file.


![image](https://github.com/user-attachments/assets/e4741a9a-ed22-4181-8238-90eeaf3141d0)

"uploaded_file" is a variable. It either holds the value **None** or containss the uploaded file's data.
st.file_uploader(...) -> creates a file upload widget. 
type=["md] -> restricts the file selection to files with .md extension.


![image](https://github.com/user-attachments/assets/4d82a490-1873-46da-b22c-6bc1f88aaeaa)

If the uploaded file in not **None**, it prepares the file for request and sends file to the server. 
I created a dictionary named "files", that is structured to be compatible with requests.post mesthod. "file" is the key and the file datails like name and binary content are the values.

requests.post(...) -> sends a HTTP POST request to the server at the mentioned URL, files = files assigns the fila data to the request ('files' variable we created). 'response' stores the server's response to the POST request. (basically the JSON result)


![image](https://github.com/user-attachments/assets/20666984-21c6-40ad-9dba-3dba00896ac6)

If server responds with a status code of 200, the request was successful. Then it extracts HTML content. 
response.json() -> converts the response body from JSON into a python dictionary.
.get("html", "") -> retrieves the value associated with the key "html". If the key does not exits then takes an empty string.


![image](https://github.com/user-attachments/assets/aab7847b-32f1-4986-a904-2f6716915e9a)

st.columns(2) -> creates 2 column layout. col1 and col2 represent left and right columns respectively. 

col1 (left side) contains converted html code and col2 (right side) contains it's preview.


![image](https://github.com/user-attachments/assets/9521ce44-d99a-45a3-acf6-5ec782ec20d0)

The else block is exceuted if the server's response status is not 200.



# converter.py

This is the main function of converting the markdown file. I've used the markdown module to convert the user-uploaded markdown file to HTML content.

The function "convert_md_to_html" takes a markdown **formatted** string as an input, and then the markdown() function is used to convert markdown text to HTML content, which is then inserted into a HTML template, to return a fully formatted HTML code.


This is how it should look
![image](https://github.com/user-attachments/assets/3ffed933-9c7e-457c-913b-e1bf81e53302)



# Instructions to run the project

## 1. Set up a virtual environment
   python3 -m venv venv (creating)
   venv\Scripts\activate (activating)

## 2. Install required python packages
   pip install -r main_requirements.txt

## 3. Setting up redis

## 4. Run the Flask backend
   python app.py

## 5. Run the streamlit frontend
   streamlit run ui.py
