from record import record_audio
from server_connection import send_audio


if __name__ == '__main__':
    recording = record_audio()
    send_audio(recording)