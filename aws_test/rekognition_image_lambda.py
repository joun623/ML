import json
import base64
import boto3
from datetime import datetime
import json

# main
def lambda_handler(event, context):
    bin_image = event["body"]
    bin_image = base64.b64decode(bin_image.encode('UTF-8'))

    # aws rekognize
    # faces = detect_labels_bynary_image(bin_image) # detect label
    faces = detect_faces(bin_image) # detect facial expression

    # save result to s3
    save_s3(bin_image, faces)

    # response
    return {
        'statusCode': 200,
        'result': faces["FaceDetails"]
    }

# labelを取得（これは人とか、これはパソコンとか）
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

# 画像と表情分析結æをS3に保存
def save_s3(image, faces):
    s3 = boto3.resource('s3')

    bucket = 'qst-rd-bucket'
    current_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    img_key = "img/" + current_time + ".jpg"
    img_obj = s3.Object(bucket, img_key)
    img_obj.put(Body=image)

    faces_key = "faces/" + current_time + ".json"
    face_obj = s3.Object(bucket, faces_key)
    face_obj.put(Body=json.dumps(faces))


    return

