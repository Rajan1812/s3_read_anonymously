import requests
import boto3
from botocore import UNSIGNED
from botocore.client import Config
s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
response=s3.list_objects(Bucket='coderbytechallengesandbox')
filename=response['Contents'][0]['Key']
res=s3.get_object(Bucket='coderbytechallengesandbox', Key=filename) # or we can directly pass the filename
output=res.get('Body').read().decode('utf-8')
print(output)
