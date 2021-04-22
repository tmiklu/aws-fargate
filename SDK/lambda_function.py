import boto3
import botocore
import json
from iac_fargate import create_fargate
from iac_service import create_service
from iac_task_definition import create_task


def get_lambda_arn(lambda_arn):
    return lambda_arn

#
##
### main program
##
#
def lambda_handler(event, context):

    lambda_arn = context.invoked_function_arn
    #print(get_lambda_arn(lambda_arn))
    #print(create_policy())
    
    ## create cluster
    create_fargate()
    
    ## create task definition
    create_task()
    
    ## create service
    #create_service()
    
    
    
    
    #return {
    #    'statusCode': 200,
    #    'body': json.dumps('Hello from Lambda!')
    #}
    #if event['Platform'] == 'lambda'
