# import cv2
# import mediapipe as mp
# import time

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_pose = mp.solutions.pose

# cap = cv2.VideoCapture(0)


# with mp_pose.Pose(
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as pose:
#     while cap.isOpened():
#         success, image = cap.read()
#         if not success:
#             print("No video in camera frame")
#             continue


#         image = cv2.flip(image, 1) # mirror the image horizontally
#         h, w, c = image.shape
#         fps_start_time = time.time()
#         fps = 0

#         image.flags.writeable = False
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         result = pose.process(image)

#         image.flags.writeable = True
#         image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#         mp_drawing.draw_landmarks(
#             image,
#             result.pose_landmarks,
#             mp_pose.POSE_CONNECTIONS,
#             landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

#         fps_end_time = time.time()
#         fps = 1 / (fps_end_time - fps_start_time) # calculate the FPS
#         cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

#         cv2.imshow("pose estimation", image)



#         if cv2.waitKey(5) & 0xFF == 27:
#             break

# cap.release()
# cv2.destroyAllWindows()




import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture('6.mp4')


with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("No video in camera frame")
            continue


        image = cv2.flip(image, 1) # mirror the image horizontally
        h, w, c = image.shape
        fps_start_time = time.time()
        fps = 0

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(
            image,
            result.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        # Give points based on landmark detection
        points = 0
        for landmark, weight in [('LEFT_ELBOW', 2), ('RIGHT_ELBOW', 2), ('LEFT_SHOULDER', 1), ('RIGHT_SHOULDER', 1)]:
            if hasattr(mp_pose.PoseLandmark, landmark):
                lm = result.pose_landmarks.landmark[getattr(mp_pose.PoseLandmark, landmark)]
                if lm.visibility > 0.5:
                    points += weight
        
        # Display the points
        cv2.putText(image, f"Points: {points}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

        fps_end_time = time.time()
        fps = 1 / (fps_end_time - fps_start_time) # calculate the FPS
        cv2.putText(image, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

        cv2.imshow("pose estimation", image)



        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()




