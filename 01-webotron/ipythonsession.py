# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation')
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='hrj-aws-botobucket',CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
new_bucket
bucket
s3
for bucket in s3.buckets.all():
    print(bucket)
    
