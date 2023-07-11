import json
import urllib.parse
import boto3
import base64
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement
    bin_img = event["body"]
    bin_img = base64.b64decode(bin_img.encode('UTF-8'))
    # bin_img = base64.b64encode(bin_img)

    # bin_img = base64.b64encode(bin_img)
    save_img_s3(bin_img)
    #bin_img = urllib.parse.unquote(bin_img).encode()

    response = detect_labels_bynary_image(bin_img)
    return {
        'statusCode': 200,
        # 'body': json.dumps('Hello from Lambda!!!!!!!!!!!!!!!!!!!')
        # 'img': bin_img
        'result': str(response)
    }

def save_img_s3(img_bin):
    s3 = boto3.resource('s3')      # ③S3オブジェクトを取得

    bucket = 'lambda-strage'    # ⑤バケット名を指定
    key = 'test_' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt'  # ⑥オブジェクトのキー情報を指定
    # file_contents = 'Lambda test'  # ⑦ファイルの内容

    obj = s3.Object(bucket,key)     # ⑧ãケット名とパスを指定
    obj.put( Body=img_bin )   # ⑨バケットにファイルを出力
    return

def detect_labels_bynary_image(image):

    client = boto3.client('rekognition')
    response = client.detect_labels(Image = {'Bytes': image})


    # print('Detected labels in ' + photo)
    for label in response['Labels']:
        print( label['Name'] + ' : ' + str(label['Confidence']))

    return response['Labels']






