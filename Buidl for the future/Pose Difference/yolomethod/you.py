import cv2
import torch
import numpy as np
# pip install yolov5from yolov5.detect import detect

model = torch.hub.load('ultralytics/yolov5', 'custom', path_or_model='yolov5s.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to half for faster inference
    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Convert BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform detection
    results = detect(model, frame, device='cpu')

    # Extract pose landmarks
    landmarks = results.pose_landmarks

    # Draw landmarks on frame
    for landmark in landmarks:
        for idx, point in enumerate(landmark):
            if point[2] > 0.5: # only draw landmarks with confidence > 0.5
                x = int(point[0] * frame.shape[1])
                y = int(point[1] * frame.shape[0])
                cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)

    # Convert RGB back to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Display frame
    cv2.imshow('Pose Estimation', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
