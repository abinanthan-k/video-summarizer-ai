import whisper


def transcribe_audio(audio_path, model):
    print("Transcribing audio...", audio_path)
    result = model.transcribe(audio_path)
    return str(result["text"])
