import base64
import boto3
import requests
import json

def image_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())

    return data.decode('utf-8')

def rekognize_test(base64_img):
    rekognition = boto3.client('rekognition')
    base64_data = base64.b64decode(base64_img.encode("utf-8"))
    faces = rekognition.detect_faces(Image={'Bytes':base64_data}, Attributes=['ALL'])
    print(faces)

def post_apigatway(base64_img, meeting_id, user_key):
    url = "https://045s8cmvf6.execute-api.ap-northeast-1.amazonaws.com/dev/image"
    # url = "https://j4es1u4kg3.execute-api.ap-northeast-1.amazonaws.com/dev/image"
    headers = {
        #'Content-type': 'image/jpeg'
        'Content-type': 'application/json'
        #'Content-type': 'multipart/form-data'
        # 'Content-type': 'application/x-www-form-urlencoded'
    }
    obj = {
        "img": base64_img,
        "meeting_id": meeting_id,
        "user_key": user_key
    }
    json_data = json.dumps(obj).encode("utf-8")

    response = requests.post(url, data=json_data, headers=headers)

    # print(response)
    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    # file_path = "meeting.jpg"
    file_path = "nature.jpg"
    base64_img = image_file_to_base64(file_path)
    meeting_id = "e5c65d4ecf62edaa674c93566db946ad5021a1f2b19637c5433ba9cc9b33536d"
    user_key = "testuserkey123"
    post_apigatway(base64_img, meeting_id, user_key)




