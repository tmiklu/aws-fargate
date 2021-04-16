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
