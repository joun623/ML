import matplotlib.pyplot as plt
import cv2

img = cv2.imread("img/Lenna.bmp")
im2 = img[150:450, 150: 450]

im2 = cv2.resize(im2, (400, 400))
cv2.imwrite("cut-resize.png", im2)

plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()
