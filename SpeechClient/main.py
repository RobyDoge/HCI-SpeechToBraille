from flask import Flask, render_template, request,redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os 
import requests

from server_connection import send_audio

from brailly import *


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

filepath = ""   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST','GET'])
def process():
    print("Processing...     ")
    print(request.method,request.form)
    if request.method == 'GET':
        return render_template('uploading.html')

    global filepath
    if 'file' not in request.files:
        return "Nicio parte de fișier"
    file = request.files['file']
    if file.filename == '':
        return "Niciun fișier selectat"
    if file and not file.filename.endswith(('.wav', '.mp3', '.flac', '.ogg')):
        return "Format invalid al fișierului"
    if not file:
        return "Niciun fișier"
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

@app.route('/record')
def record_message():
    return render_template('record.html')


@app.route('/get-braille-translation')
def get_braille_translation():
    quote, _ = get_random_quote()   # Assuming this function retrieves a random quote
    braille_translation = translate_to_braille(quote)   # Assuming this function translates to Braille
    romanian_translation = translate_text(quote)
    return jsonify({"brailleTranslation": f"{romanian_translation}\n\n||\nV\n\n{braille_translation}"})

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True, port=5000)