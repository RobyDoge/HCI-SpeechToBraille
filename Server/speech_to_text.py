# import whisper

# model = whisper.load_model("small")

class Transcriber:
    pass
#     def __init__(self):
#         pass

#     def convert(self, audio):
#         audio = whisper.load_audio(audio)
#         audio = whisper.pad_or_trim(audio)

#         mel = whisper.log_mel_spectrogram(audio).to(model.device)

#         _, probs = model.detect_language(mel)
#         print(f"Detected language: {max(probs, key=probs.get)}")

#         options = whisper.DecodingOptions(fp16=False)

#         try:
#             result = whisper.decode(model, mel, options)
#             return result.text

#         except Exception as e:
#             return f"Exception encountered; {str(e)}"
