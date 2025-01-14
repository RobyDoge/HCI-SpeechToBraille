import whisper

model = whisper.load_model("small")


def transcribe(audio):
    # time.sleep(3)
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16=False)

    try:
        result = whisper.decode(model, mel, options)
        return result.text

    except Exception as e:
        return f"Exception encountered; {str(e)}"


# gr.Interface(
#     title='OpenAI Whisper ASR Gradio Web UI',
#     fn=transcribe,
#     inputs=[
#         gr.inputs.Audio(source="microphone", type="filepath")
#     ],
#     outputs=[
#         "textbox"
#     ],
#     live=True).launch(debug=True)
#     # live=True).launch(debug=True)

result = transcribe('pulanjs.wav')
print(result)
