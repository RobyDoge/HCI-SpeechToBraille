from flask import Flask, render_template
import threading

from server_conection import get_text
from send_text import send_text

app = Flask(__name__)

messages_list = ["test message"]

@app.route('/')
def index():
    return render_template('index.html', messages=messages_list)

def update_messages():
    def aux():
        while True:
            #await getting a text, when u do send them to arduino and update the messages_list
            pass
    thread = threading.Thread(target=aux)
    thread.daemon = True
    thread.start()

if __name__ == '__main__':
    update_messages()
    app.run(debug=True, port=5001)


