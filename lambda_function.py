import json
import logging
import boto3
import botocore

logging.getLogger().setLevel(logging.INFO)

BUCKET_NAME = 'dev-days-test'
KEY = 'hello.txt'

s3 = boto3.resource('s3')

def lambda_handler(event, context):

    logging.info(event)
# TODO implement

    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, '/tmp/hello_local.txt')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            logging.error("The object does not exist,")
        else:
            raise

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
}
