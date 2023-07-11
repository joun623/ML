import matplotlib.pyplot as plt
import cv2

img = cv2.imread("img/Lenna.bmp")
im2 = cv2.resize(img, (600, 300))

cv2.imwrite("out-resize.png", im2)

plt.imshow(cv2.cvtColor(im2, cv2.COLOR_BGR2RGB))
plt.show()
