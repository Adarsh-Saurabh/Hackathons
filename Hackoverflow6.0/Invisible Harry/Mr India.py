# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# back = cv2.imread("image.jpg")
# while cap.isOpened():
#     ret , frame = cap.read()
#     if ret:
#         hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#         l_red = np.array([0,0,0])
#         u_red = np.array([90,256,256])
#         mask = cv2.inRange(hsv,l_red,u_red)
#         mask1 = cv2.inRange(hsv,l_red,u_red)
#         part1 = cv2.bitwise_and(back,back,mask = mask)
#         mask = cv2.bitwise_not(mask)
#         part2 = cv2.bitwise_and(frame,frame,mask = mask)
#         cv2.imshow("I am Mr.INDIA.....",part2 + part1 )
#         if cv2.waitKey(5) == ord('q'):
#             break
# cap.release()
# cv2.destroyAllWindows()




import cv2
import numpy as np

# Load the background image
back = cv2.imread("image.jpg")

# Check if the image was loaded successfully
if back is None:
    print("Error loading image")
    exit()

# Create a window to display the output
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Output", 1000, 800) 

# Capture video from default camera
cap = cv2.VideoCapture(0)



# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Define the range of red color in HSV
l_red = np.array([0, 20, 70])
u_red = np.array([30, 255, 255])

# Start the video capture loop
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error reading frame")
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to extract the red color
    mask = cv2.inRange(hsv, l_red, u_red)

    # Perform bitwise and between the background and the mask
    part1 = cv2.bitwise_and(back, back, mask=mask)

    # Perform bitwise and between the frame and the inverted mask
    mask_inv = cv2.bitwise_not(mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Combine the two parts
    output = cv2.add(part1, part2)

    # Display the output
    cv2.imshow("Output", output)

    # Check for key press
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()

