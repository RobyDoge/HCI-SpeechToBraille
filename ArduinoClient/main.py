from flask import Flask, render_template
import requests

from send_text import send_text

app = Flask(__name__)

messages_list = ["test message"] 

@app.route('/')
def index():
    return render_template('index.html', messages=messages_list)

@app.route('/get_message')
def get_message():
    url = 'http://127.0.0.1:6969/get_message'
    response = requests.get(url)

    responsodata = response.json()
    message = responsodata['message']
    messages_list.append(message)
    send_text(message)
    return render_template('index.html', messages=messages_list)
 
if __name__ == '__main__':
    app.run(debug=True, port=5001)
