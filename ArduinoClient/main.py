from send_text import send_text
from server_conection import get_text

if __name__ == '__main__':
    text = get_text()
    send_text(text)


