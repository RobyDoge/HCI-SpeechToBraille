import copy
import os.path
import wave

import pyaudio
import whisper


class Converter:
    def __init__(self, model_size="small", chunk=1024, audio_format=pyaudio.paInt16, channels=1, rate=16000):
        self._chunk = chunk
        self._audio_format = audio_format
        self._channels = channels
        self._rate = rate

        self._model_size = model_size
        self._model = whisper.load_model(self._model_size)

        self._recordings_path = os.path.join(os.path.dirname(__file__), "Recordings")

    def record_audio(self, filename, duration):
        audio = pyaudio.PyAudio()

        stream = audio.open(format=self._audio_format, channels=self._channels, rate=self._rate, input=True, frames_per_buffer=self._chunk)

        print("Say sum @.@")
        frames = []

        for _ in range(0, int(self._rate / self._chunk * duration)):
            data = stream.read(self._chunk)
            frames.append(data)

        print("Got it -_-")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        with wave.open(os.path.join(self._recordings_path, filename), 'wb') as wf:
            wf.setnchannels(self._channels)
            wf.setsampwidth(audio.get_sample_size(self._audio_format))
            wf.setframerate(self._rate)
            wf.writeframes(b''.join(frames))

        print(f"Saved recording at {os.path.join(self._recordings_path, filename)}")

    def transcribe(self, audio):
        # time.sleep(3)
        # load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(audio)
        audio = whisper.pad_or_trim(audio)

        # make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(self._model.device)

        # detect the spoken language
        _, probs = self._model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions(fp16=False)

        try:
            result = whisper.decode(self._model, mel, options)
            return result.text

        except Exception as e:
            return f"Exception encountered; {str(e)}"

    def transcribe_all(self):
        for filename in os.listdir(self._recordings_path):
            result = self.transcribe(os.path.join(self._recordings_path, filename))

            print(f"Transcription of {filename} =>\n\n{result}")

    def find_unique_filename(self, filename):
        if filename in os.listdir(self._recordings_path):
            initial_base_name = copy.copy(filename.split(".")[0])
            counter = 1

            while filename in os.listdir(self._recordings_path):
                filename = f"{initial_base_name + str(counter)}.wav"

                counter += 1

        return filename


my_converter = Converter()

my_converter.record_audio(my_converter.find_unique_filename("pulanjs.wav"), duration=5)
my_converter.transcribe_all()
