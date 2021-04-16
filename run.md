# create role 
```
aws iam --region us-west-2 create-role --role-name ecsTaskExecutionRole --assume-role-policy-document file://task-execution-assume-role.json 
```
# attach policy
```
aws iam --region us-west-2 attach-role-policy --role-name ecsTaskExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy 
```

# create config ~/.ecs/config 
```
ecs-cli configure --cluster tutorial --default-launch-type FARGATE --config-name tutorial --region us-east-1 
```

# IMPORTANT, set env vars for access and secret key 
```
ecs-cli configure profile --access-key AWS_ACCESS_KEY_ID --secret-key AWS_SECRET_ACCESS_KEY 
``` 

# create empty fargate cluster with vpc and two subnets 
```
ecs-cli up --cluster-config tutorial
``` 
