import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    print(frame)
    frame = cv2.resize(frame, (500, 300))
    cv2.imshow('OpenCV Web Camera', frame)
    k = cv2.waitKey(1)
    if k == 27 or k == 13: break

cap.release()
cv2.destroyAllWindows()
