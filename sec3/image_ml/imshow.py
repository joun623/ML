import matplotlib.pyplot as plt
import cv2
img = cv2.imread("lenna.bmp")

plt.axis("off")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
