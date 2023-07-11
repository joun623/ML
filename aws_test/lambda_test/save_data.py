import boto3
from datetime import datetime
import json
import decimal

# 画像と表情分析結をS3に保存
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

def insert_dynamody(meeting_id, rekognize_json):
    # データ準備
    dt_now = datetime.now()
    #rekognize_decimal = json.loads(str(rekognize_json), parse_float=decimal.Decimal)
    item = {
        "meeting_key": meeting_id,
        "analysis_datetime": dt_now.strftime("%Y-%m-%dT%H:%M:%S"),
        "analysis_result": str(rekognize_json)
    }
    #primary_key = {"primary": meeting_id} #テーブル名

    # db insert

    dynamodb = boto3.resource('dynamodb') #使うリソースを選んでおく
    table_name = "t_analytical_data" #テーブル名
    dynamo_table = dynamodb.Table(table_name)
    dynamo_table.put_item(Item=item)

    return
