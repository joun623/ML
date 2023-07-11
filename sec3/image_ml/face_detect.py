import matplotlib.pyplot as plt
import cv2

def face_detect(img):
    # 顔分類器生成
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    # 画像読み込み
    # img = cv2.imread(img_name)

    # 白黒変換
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 顔検出
    face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))

    if len(face_list) == 0:
        print("face-detect failed")
        quit()


    return face_list

if __name__ == "__main__":
    img_name = "img/mono/WOMAN.bmp"
    img = cv2.imread(img_name)
    face_list = face_detect(img)

    for (x, y, w, h) in face_list:
            print("顔の座標=", x, y, w, h)
            red = (0, 0, 255)
            cv2.rectangle(img, (x, y), (x+w, y+h), red, thickness=20)

    cv2.imwrite("face-detect.png", img)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
