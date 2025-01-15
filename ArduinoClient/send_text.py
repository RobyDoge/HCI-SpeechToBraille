import serial
import time

# Maparea caracterelor la Braille (identic cu Arduino)
braille_map = {
    'a': 0b010000, 'b': 0b010100, 'c': 0b110000, 'd': 0b111000, 'e': 0b011000,
    'f': 0b110100, 'g': 0b111100, 'h': 0b011100, 'i': 0b011000, 'j': 0b101100,
    'k': 0b010001, 'l': 0b010101, 'm': 0b110001, 'n': 0b111001, 'o': 0b011001,
    'p': 0b110101, 'q': 0b111101, 'r': 0b011101, 's': 0b101001, 't': 0b101101,
    'u': 0b010011, 'v': 0b010111, 'w': 0b101110, 'x': 0b110011, 'y': 0b111011,
    'z': 0b011011, ' ': 0b000000, '.': 0b001101, ',': 0b001000
}

def char_to_braille(char):
    char = char.lower()
    return braille_map.get(char, -1) # Returnează 0 dacă caracterul nu e găsit

def send_braille(ser, braille_code):
    ser.write(str(braille_code).encode()) # Trimite codul ca string prin serială
    ser.write(b'\n') # Trimite un newline pentru a fi detectat de Serial.parseInt()

def send_text(text):
    try:
        ser = serial.Serial('COM3', 9600)  # Înlocuiește cu portul serial corect (ex. COM3 pe Windows)
        time.sleep(2) # Așteaptă conectarea serială

        for char in text:
            braille_code = char_to_braille(char)
            if braille_code != -1:
                send_braille(ser, braille_code)
                time.sleep(2)
            else:
                print(f"Caracterul '{char}' nu are corespondent Braille.")

        send_braille(ser, 0b000000)

        
        ser.close()
        print("Transmitere terminată.")

    except serial.SerialException as e:
        print(f"Eroare la conectarea serială: {e}")
