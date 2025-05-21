import uuid
import os
from moviepy import VideoFileClip

def extract_audio(video_path, output_dir="uploads"):
    print("Extracting audio...")
    os.makedirs(output_dir, exist_ok=True)
    unique_filename = f"{video_path}_audio.wav"
    output_audio_path = os.path.join(output_dir, unique_filename)
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    print(output_audio_path)
    return output_audio_path
