
"""
    aws_rekognize  APIを使用して、画像認識した結果を取得する
"""
import boto3

# labelを取得（ここは人とか、これはパソコンとか）
def detect_labels_bynary_image(image):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image = {'Bytes': image})

    return response

# 表情分析
def detect_faces(image):
    client = boto3.client('rekognition')
    faces = client.detect_faces(
        Image={'Bytes': image},
        Attributes=['ALL']
        )

    return faces
