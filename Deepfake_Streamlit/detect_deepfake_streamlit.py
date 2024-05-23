import tensorflow as tf
import cv2
import streamlit as st

def detect_deepfake(video_path, model_path, threshold=0.5):
    model = tf.keras.models.load_model(model_path)
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fake_frames = 0
    total_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_resized = cv2.resize(frame, (128, 128))
        frame_rescaled = frame_resized / 255.0
        prediction = model.predict(tf.expand_dims(frame_rescaled, axis=0))
        if prediction > threshold:
            fake_frames += 1
        total_frames += 1

    cap.release()
    return fake_frames, total_frames

st.title("Deepfake Detection - Detection")

video = st.file_uploader("Upload Video for Detection", type=["mp4", "avi", "mov"])

if st.button("Detect Deepfake"):
    if video is not None:
        with open("new_video.mp4", "wb") as f:
            f.write(video.read())
        fake_frames, total_frames = detect_deepfake('new_video.mp4', 'deepfake_detection_model.h5')
        st.write(f"Fake frames: {fake_frames}/{total_frames}")
    else:
        st.error("Please upload a video.")
