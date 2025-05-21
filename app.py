import streamlit as st
from pathlib import Path
import whisper

from utils.audio_extract import extract_audio
from utils.transcribe import transcribe_audio
from utils.summarize import summarize_text

st.set_page_config(page_title="Video Summarizer AI", layout="centered")

st.title("🎬 Video Summarizer AI")
st.write("Upload a video file to get a summarized transcription.")

uploaded_file = st.file_uploader("Upload your video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    with st.spinner("Saving uploaded video..."):
        video_path = Path("temp_video.mp4")
        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

    with st.spinner("Extracting audio..."):
        audio = extract_audio(video_path)

    with st.spinner("Loading Whisper model..."):
        model = whisper.load_model("tiny")

    with st.spinner("Transcribing audio..."):
        text = transcribe_audio(audio, model)

    st.subheader("📄 Transcription")
    st.text_area("Full Transcript", text, height=200)

    with st.spinner("Summarizing transcription..."):
        summary = summarize_text(text)

    st.subheader("🧠 Summary")
    st.success(summary)
    video_path.unlink()
