from detect_zip import *
import matplotlib.pyplot as plt

from sklearn.externals import joblib

clf = joblib.load("digits.pkl")

cnts, img = detect_zipno("hagaki1.png")

for i, pt in enumerate(cnts):
    x, y, w, h = pt
    x += 8
    y += 8
    w -= 16
    h -= 16
    im2 = img[y: y+h, x:x+w]
    im2gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
    im2gray = cv2.resize(im2gray, (8,8))
    im2gray = 15 - im2gray // 16
    im2gray = im2gray.reshape((-1, 64))

    res = clf.predict(im2gray)

    plt.subplot(1, 7, i + 1)
    plt.imshow(im2)
    plt.axis("off")
    plt.title(res)
plt.show()
