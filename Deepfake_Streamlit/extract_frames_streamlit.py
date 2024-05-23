import cv2
import os
import streamlit as st

def extract_frames(video_path, output_folder, frame_rate=1):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    while cap.isOpened():
        frame_id = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        ret, frame = cap.read()
        if not ret:
            break
        if frame_id % frame_rate == 0:
            filename = os.path.join(output_folder, f"frame_{count:04d}.jpg")
            cv2.imwrite(filename, frame)
            count += 1
    cap.release()

st.title("Deepfake Detection - Frame Extraction")

real_video = st.file_uploader("Upload Real Video", type=["mp4", "avi", "mov"])
fake_video = st.file_uploader("Upload Fake Video", type=["mp4", "avi", "mov"])

if st.button("Extract Frames"):
    if real_video is not None and fake_video is not None:
        with open("real_video.mp4", "wb") as f:
            f.write(real_video.read())
        with open("fake_video.mp4", "wb") as f:
            f.write(fake_video.read())
        extract_frames('real_video.mp4', 'output_frames_folder/real')
        extract_frames('fake_video.mp4', 'output_frames_folder/fake')
        st.success("Frame extraction completed.")
    else:
        st.error("Please upload both videos.")
