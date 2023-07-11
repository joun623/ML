import json
import base64

from rekognition import Rekognition
from aws_rekognize import detect_labels_bynary_image, detect_faces
from save_data import save_s3, insert_dynamody

# main
def lambda_handler(event, context):
    bin_image =  event["body"]["img"]
    meeting_id = event["body"]["meeting_id"]
    bin_image = base64.b64decode(bin_image.encode('utf-8'))

    # aws rekognize
    #faces = detect_labels_bynary_image(bin_image["file"]) # detect label
    faces = detect_faces(bin_image) # detect facial expression
    faces_result = [str(Rekognition(face)) for face in faces["FaceDetails"]]
    # save result to s3
    #save_s3(bin_image, faces)
    insert_dynamody(meeting_id, faces)
    # response
    return {
        'statusCode': 200,
        'result': str(faces_result),
        'meeting_id': meeting_id
    }
