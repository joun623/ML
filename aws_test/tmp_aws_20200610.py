import json
import base64
import boto3
from datetime import datetime
import json
import urllib.parse

def fix_confidence(is_satisfy_condition, confidence):
    """
        0.0 ~ 100.0の範囲で, is_satisfy_conditionがFalseのとき
        confidenceを反転する

        (ex...
        is_satisfy_condition: True,  confidence: 74.5 => return 74.5(そのまま)
        is_satisfy_condition: False, confidence: 74.5 => return 25.5(50に対して反転)
    """
    float_confidence = float(confidence)

    if is_satisfy_condition:
        return float_confidence
    else:
        return 100.0 - float_confidence

class RekognitionResult:
    """
        aws rekognitionで得た情報(json)を整理
        1人分（実際にはリストで画像に写ってる人数分くる)
    """
    def __init__(self, rekog_params):

        ### 感情
        self.emotions = {emotion["Type"]: float(emotion["Confidence"]) for emotion in rekog_params["Emotions"]}

        ### 顔の位置
        self.bounding_box = rekog_params["BoundingBox"]

        ### 年齢予測{low:~, high:~}
        self.age_range = rekog_params["AgeRange"]

        ### この辺使うかも
        self.quality = rekog_params["Quality"]
        self.confidence = rekog_params["Confidence"]


        # 目はどの位置とか口はどことかそう言う情報
        self.landmarks = rekog_params["Landmarks"]
        # ???
        self.pose = rekog_params["Pose"]


        ### 人物の特徴
        def calc_feature_confidence(parameter, is_gender=False):
            '''
                特徴量の形式を
                    (True/False, confidence(0.5~1.0))
                から
                    (confidence(0.0~1.0))
                にする
            '''
            if is_gender:
                # MaleにするかFemaleにするかでまあまあ悩んだ
                is_satisfy_condition = (parameter["Value"] == "Female")
            else:
                is_satisfy_condition = parameter["Value"]

            return fix_confidence(is_satisfy_condition, parameter['Confidence'])


        self.features = {
            "eye_glasses": calc_feature_confidence(rekog_params["Eyeglasses"]), # メガネ
            "sun_glasses": calc_feature_confidence(rekog_params["Sunglasses"]), # サングラス
            "gender":      calc_feature_confidence(rekog_params["Gender"], is_gender=True), # 性
            "beard":       calc_feature_confidence(rekog_params["Beard"]),    # ひげ
            "mustache":    calc_feature_confidence(rekog_params["Mustache"]), # 顎ひげ
            "eyes_open":   calc_feature_confidence(rekog_params["EyesOpen"]), # 目の開き
            "mouth_open":  calc_feature_confidence(rekog_params["MouthOpen"]) # 口の開き
        }

    def __repr__(self):
        ret_words = "Class of Aws Rekognize Result\n"
        ret_words += str(self.features)
        if hasattr(self, "emotions"):
            ret_words += "ex. emotion is " + str(self.emotions)

        return ret_words

    def __str__(self):
        return str(dict(self.emotions, **self.features))



# main
def lambda_handler(event, context):
    # bin_image = str(type(event["queryParameters"]))
    #bin_image = event["queryParameters"]

    #bin_image = event["queryParameters"]["img"].encode('UTF-8')
    bin_image =  event["body"]["img"]
    #bin_image = bin_image.encode("utf-8")
    #bin_image = base64.b64decode(bin_image)
    #bin_image = event["queryParameters"]["img"]
    #bin_image = bin_image + '=' * (-len(bin_image) % 4)
    #bin_image = bin_image.replace("%", r"\x")
    #bin_image = bin_image.encode()
    #bin_image = base64.urlsafe_b64decode(bin_image)
    #bin_image = bin_image.decode(encoding='utf-8')
    bin_image = base64.b64decode(bin_image.encode('utf-8'))


    #data_dict = {}
    #for data in str(bin_image).split("&"):
    #    key, value = data.split("=")
    #    data_dict[key] = value


    # bin_image = urllib.parse.unquote(bin_image, encoding='UTF-8')
    #bin_image =  data_dict["img"].replace("%", r"\x")
    #bin_image = str(bin_image).replace('&', ',')
    #faces = detect_faces(bin_image)
    #bin_image = json.loads(bin_image)["img"]
    #if False:
    #bin_image = base64.b64decode(bin_image.encode('UTF-8'))

    # aws rekognize
    #faces = detect_labels_bynary_image(bin_image["file"]) # detect label
    faces = detect_faces(bin_image) # detect facial expression

    #faces_result = [str(RekognitionResult(face)) for face in faces["FaceDetails"]]
    # save result to s3
    #save_s3(bin_image, faces)

    # response
    return {
        'statusCode': 200,
        #'result': faces_result[0]
        #'result': bin_image
        'result': faces
    }

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

def insert_dynamody():
    dynamodb = boto3.resource('dynamodb') #使うリソースを選んでおく
    table_name = "t_analytical_data" #テーブル名
    primary_key = {"primary": event["body"]} #テーブル名
    dynamotable = dynamodb.Table(table_name)
    res = dynamotable.get_item(Key=primary_key) #指定したprymaryで検索して結果を取得
    item = res["Item"] #要素を指定してないので全部

    return item
