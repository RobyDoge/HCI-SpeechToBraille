import pyaudio
import wave

def record_audio(filename, duration):
    # Set up parameters for recording
    chunk = 1024  # Number of audio samples per frame
    format = pyaudio.paInt16  # Audio format (16-bit PCM)
    channels = 1  # Mono audio
    rate = 44100  # Sample rate (Hz)

    # Create a PyAudio object
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))