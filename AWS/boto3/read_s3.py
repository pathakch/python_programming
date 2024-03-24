import boto3
import json

s3 = boto3.resource('s3')
bucket_name = 'myfirst-demo-s3bucket'
file_object = s3.Object(bucket_name,'test_json_file.json')
contents = file_object.get()['Body'].read().decode('utf-8')
json_data = json.loads(contents)
print(json_data['info'])