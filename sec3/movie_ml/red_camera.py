import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (500, 300))

    frame[:, :, 0] = 0
    frame[:, :, 1] = 0

    cv2.imshow('RED camera', frame)
    if cv2.waitKey(1) == 13: break

cap.release()
cv2.destroyAllWindows()


