import boto3
import json

s3 = boto3.resource('s3')

bucket_name = 'my-demo-bucket123321'

file_object = s3.Object(bucket_name,'information.txt')

contents = file_object.get()['Body'].read().decode('utf-8')

json_data = json.loads(contents)

print(json_data['info'])