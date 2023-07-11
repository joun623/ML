import boto3
import base64


def detect_labels_local_file(photo):

    client = boto3.client('rekognition')

    with open(photo, 'r') as image:
        decode_read = base64.b64decode(image.read())
        response = client.detect_labels(Image = {'Bytes': decode_read})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print( label['Name'] + ' : ' + str(label['Confidence']))

    return response['Labels']

def detect_faces(photo):
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = cli

def main():
    photo = 'meeting_dl.jpg'

    label_count=detect_labels_local_file(photo)
    print("Lables detected: " + str(label_count))

if __name__ == '__main__':
    main()
