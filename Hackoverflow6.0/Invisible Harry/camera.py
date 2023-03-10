import cv2
print("Welcome to Harry Potter's invisible world!")
print("For this to work you need to Run this file first then press 'q' for taking a picture of background")
print("press 'q' to take a picture and then the program will quit itself")
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, back = cap.read()
    if ret :
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord("q"):
            cv2.imwrite("image.jpg", back)
            break

        
cap.release()
cv2.destroyAllWindows()






