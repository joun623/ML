import requests
import json

url = "https://j4es1u4kg3.execute-api.ap-northeast-1.amazonaws.com/dev"
file_path = "meeting.jpg"

with open(file_path, 'rb') as image:
    byte_str = image.read()
    # response = client.detect_labels(Image = {'Bytes': image.read()})

with open("row_data.txt", "w") as f:
    f.write(str(byte_str))
headers = {
        'Content-type': 'image/jpeg'
        # 'Content-type': 'multipart/form-data'
        # 'Content-type': 'application/x-www-form-urlencoded'
    }
# response = requests.post(url, data={"img": byte_str, "url": "hoge"}, headers=headers)
response = requests.post(url, data={"img": byte_str, "url": "hoge"}, headers=headers)
# response = requests.post(url, data={"img": "hello !!!"})
print(response.status_code)
print(response.text)
