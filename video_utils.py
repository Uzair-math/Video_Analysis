import cv2

def extract_frames(video_path, interval_sec=3):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = []
    timestamps = []
    if not cap.isOpened():
        raise Exception("Error opening video file")
    frame_count = 0
    frame_interval = int(fps * interval_sec)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            frames.append(frame)
            timestamps.append(frame_count / fps)
        frame_count += 1
    cap.release()
    return frames, timestamps
