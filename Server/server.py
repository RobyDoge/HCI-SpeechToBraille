from flask import Flask, render_template, request
import os

from speech_to_text import Transcriber

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and not file.filename.endswith(('.wav', '.mp3', '.flac', '.ogg')):
        return "Invalid file format"
    if not file:
        return "No file"
    
    #transcriber = Transcriber()
    result = 'test'#transcriber.transcribe(file)
    print(result)
    return render_template('upload_successful.html')


@app.route('/record', methods=['POST'])
def record_message():
    # This endpoint can be implemented to handle audio recording data.
    return "Recording functionality not yet implemented."

if __name__ == '__main__':
    app.run(debug=True)