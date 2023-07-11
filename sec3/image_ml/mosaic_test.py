import matplotlib.pyplot as plt
import cv2
from mosaic import mosaic as mosaic
from face_detect import face_detect as face_detect

img_name = "img/mono/WOMAN.bmp"
img = cv2.imread(img_name)
face_list = face_detect(img)
x, y, w, h = face_list[0]
face_rectangle = (x, y, x + w, y + h)
mos = mosaic(img, face_rectangle, 10)

cv2.imwrite("WOMAN-mosaic.png", mos)
plt.imshow(cv2.cvtColor(mos, cv2.COLOR_BGR2RGB))
plt.show()
