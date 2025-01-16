import requests

def send_audio(filepath):
    url = 'http://localhost:6969/upload'
    print(filepath)
    files = {'audio': open(filepath, 'rb')}
    print(files)
    response = requests.post(url, files=files)

    print(response.text)