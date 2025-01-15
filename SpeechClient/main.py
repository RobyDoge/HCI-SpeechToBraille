from flask import Flask, render_template, request,redirect, url_for
from werkzeug.utils import secure_filename
import time
import os 

from record import record_audio
from server_connection import send_audio


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

filepath = ""   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    global filepath
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and not file.filename.endswith(('.wav', '.mp3', '.flac', '.ogg')):
        return "Invalid file format"
    if not file:
        return "No file"
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    print (f"File saved to {filepath}")
    return render_template('uploading.html')

@app.route('/execute')
def execute():
    global filepath
    send_audio(filepath)
    return redirect(url_for('upload'))

@app.route('/upload')
def upload():
    return render_template('upload_successful.html')




@app.route('/record', methods=['POST'])
def record_message():
    # This endpoint can be implemented to handle audio recording data.
    return "Recording functionality not yet implemented."

if __name__ == '__main__':
    app.run(debug=True, port=5000)