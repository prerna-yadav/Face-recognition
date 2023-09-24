import cv2
cap=cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,720)

imgBackground=cv2.imread('Resources/background.png')

while True:
    success,img=cap.read()
    cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    cv2.waitKey(1)
