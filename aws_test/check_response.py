import json

json_open = open('response.json', "r")
json_load = json.load(json_open)

print([item['analysis_datetime'] for item in json_load['rekognize_result']['Items']])



