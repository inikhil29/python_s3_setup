from dotenv.main import load_dotenv
import boto3
import os

def get_s3_env_variables():
        load_dotenv()
        return {
            "aws_access_key": os.environ["S3_ACCESS_KEY_ID"],
            "aws_secret_key": os.environ["S3_SECRET_ACCESS_KEY"],
            "region": os.environ["S3_REGION"],
        }

def initialize_s3_resource(aws_access_key, aws_secret_key, region):
    s3_resource = boto3.resource(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region,
    )
    return s3_resource    
