import boto3
import botocore

from powerlibs.aws.λ.deployer import helpers
from powerlibs.aws.λ.deployer import settings
from powerlibs.aws.λ.deployer.log import logger

try:
    lambda_client = boto3.client('lambda')
except (botocore.exceptions.NoRegionError, botocore.exceptions.NoCredentialsError):
    credentials_kwargs = {
        'aws_access_key_id': settings.AWS_ACCESS_KEY_ID,
        'aws_secret_access_key': settings.AWS_SECRET_ACCESS_KEY,
        'region_name': settings.AWS_REGION_NAME,
    }
    lambda_client = boto3.client('lambda', **credentials_kwargs)


def push_lambda(zip_file, lambda_settings):
    kwargs = lambda_settings
    if settings.ENV_FILE:
        kwargs = {**kwargs, 'Environment': {'Variables': helpers.read_env_vars(settings.ENV_FILE)}}
    try:
        update_function(zip_file, **kwargs)
    except botocore.exceptions.ClientError:  # if function doesn't exist yet
        logger.info('Lambda doesn\'t exist, creating it...')
        lambda_client.create_function(Code={'ZipFile': open(zip_file, 'rb').read()}, **kwargs)


def update_function(zip_file, **kwargs):
    "Raises ClientError if fuction doesn't exist"
    lambda_client.get_function(FunctionName=kwargs['FunctionName'])  # assert exists
    logger.info('Lambda exists, updating it...')
    lambda_client.update_function_code(
        FunctionName=kwargs['FunctionName'],
        ZipFile=open(zip_file, 'rb').read(),
    )
    lambda_client.update_function_configuration(**kwargs)
