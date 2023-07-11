
"""
   aws rekognizeで帰ってきたデータを整理保存する
"""



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



class Rekognition:
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


