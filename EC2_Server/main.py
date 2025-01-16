from flask import Flask, request, jsonify
import whisper
import requests

app = Flask(__name__)

message = ''

model = whisper.load_model("small")

def transcribe(audio):
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions(fp16=False)

    try:
        result = whisper.decode(model, mel, options)
        return result.text
    except Exception as e:
        return f"Exception encountered: {str(e)}"

@app.route('/upload', methods=['POST'])
def upload_audio():
    file = request.files['audio']
    file.save("****.wav")
    
    transcript = transcribe('****.wav')
    global message
    message = transcript
    return jsonify({'transcript': transcript})

@app.route('/get_message', methods=['GET'])
def get_message():
    global message
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
