import streamlit as st
import tempfile
from video_utils import extract_frames
from groq_client import analyze_frame_with_groq

st.title("Video Analysis using AI")
st.write("Upload an .mp4 video, and the AI will describe what is happening in the frames.")

video_file = st.file_uploader("Upload a video file", type=["mp4"])

if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    video_path = tfile.name

    st.info("Extracting frames...")
    frames, timestamps = extract_frames(video_path, interval_sec=3)
    st.success(f"Extracted {len(frames)} frames")

    descriptions = []
    with st.spinner("Analyzing frames with Groq AI..."):
        for i, frame in enumerate(frames):
            desc = analyze_frame_with_groq(frame)
            descriptions.append((timestamps[i], desc))

    st.header("Video Scene Description")
    for timestamp, desc in descriptions:
        st.write(f"[{timestamp:.2f} sec] Description: {desc}")
