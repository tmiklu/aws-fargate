import boto3

client = boto3.client('ecs')

def create_service():
  response = client.create_service(
      cluster='vls-demo-fargate',
      serviceName='vls-dev',
      taskDefinition='vls-dev',

      desiredCount=1,
      launchType='FARGATE',

      platformVersion='1.4.0',

      networkConfiguration={
          'awsvpcConfiguration': {
              'subnets': [
                  'string',
              ],
              'securityGroups': [
                  'string',
              ],
              'assignPublicIp': 'DISABLED'
          }
      },
      tags=[
          {
              'key': 'env',
              'value': 'dev'
          },
      ]
  )
