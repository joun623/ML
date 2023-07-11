import cv2
from sklearn.externals import joblib

def predict_digit(filename):
    clf = joblib.load("digits.pkl")
    my_img = cv2.imread(filename)
    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)
    my_img = cv2.resize(my_img, (8, 8))
    my_img = 15 - my_img // 16

    my_img = my_img.reshape((-1, 64))
    res = clf.predict(my_img)
    return res[0]

n = predict_digit("eight.bmp")
print("my8.png = " + str(n))

