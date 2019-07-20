import boto3
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():  #this wraps the functions (group)
    "Webotron deploys the website to AWS"
    pass

@cli.command('list-buckets') # we use cli rather than than click, since cli wraps the function
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)
#
# @cli.command('list-bucket-objects')
# def list_bucket_objects():
#     "Lists bucket objects"
#     for obj in s3.Bucket('myhrjbuckert').objects.all():
#         print(obj)

@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "Lists bucket objects"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ =='__main__':
    cli() #again we just call cli.
