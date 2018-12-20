import cv2
import numpy as np

cap = cv2.VideoCapture("test.avi")
cap2 = cv2.VideoCapture("blue.avi")

while True:
    ret, frame2 = cap2.read()
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerGreen = np.array([45, 50, 100])
    higherGreen = np.array([75, 255, 255])

    mask = cv2.inRange(hsv, lowerGreen, higherGreen)
    maskinv = 255 - mask

    res2 = cv2.bitwise_and(frame2, frame2, mask=mask)
    res = cv2.bitwise_and(frame, frame, mask= maskinv)
    dst = cv2.add(res, res2)

    cv2.imshow("hi mom", dst)
    if cv2.waitKey(6) & 0xFF == ord('q'):
        break


