from speech_to_text import Transcriber
import threading
import time


class SpeechToArduino:
    def speech_to_text(self, filepath):
        transcriber = Transcriber()
        return transcriber.convert(filepath)
    
    def text_to_arduino(self, text):
        with open('start.txt', 'w') as file:
            file.truncate(0)
            file.write('start')
        with open('arduino.txt', 'w') as file:
            file.write(text)

        def countdown_and_reset():
            text_lenght = len(text)
            time_to_display_symbol = 0.25
            timer = text_lenght * time_to_display_symbol 
            time.sleep(timer)  
            self.reset()

        thread = threading.Thread(target=countdown_and_reset)
        thread.start()
        
    def reset(self):
        with open('start.txt', 'w') as file:
            file.truncate(0)
            file.write('reset')
        with open('arduino.txt', 'w') as file:
            file.truncate(0)
            file.write('')
    
    