import boto3
import botocore
import json
from iac_fargate import create_fargate
from iac_service import create_service
from iac_task_definition import create_task

pipeline = boto3.client('codepipeline')
ssm      = boto3.client('ssm')


#
##
### main program
##
#
def lambda_handler(event, context):
    response = ssm.get_parameters(
        Names=[
            'PLATFORM',
        ],
        WithDecryption=False
    )
    
    if response['Parameters'][0]['Value'] == 'Fargate':
        create_fargate()
        create_task()
        create_service()
    
    elif response['Parameters'][0]['Value'] == 'Lambda':
        print('Deploy to lambda')
    
    else:
        print('Not supported AWS compute platform')
        
    
    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return response
