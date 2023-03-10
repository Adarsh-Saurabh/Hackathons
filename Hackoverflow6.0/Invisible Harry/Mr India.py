import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread("image.jpg")
while cap.isOpened():
    ret , frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_red = np.array([0,0,0])
        u_red = np.array([90,256,256])
        mask = cv2.inRange(hsv,l_red,u_red)
        mask1 = cv2.inRange(hsv,l_red,u_red)
        part1 = cv2.bitwise_and(back,back,mask = mask)
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame,frame,mask = mask)
        cv2.imshow("I am Mr.INDIA.....",part2 + part1 )
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
