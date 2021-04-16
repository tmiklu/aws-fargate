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

# copy vpc id from previous command 
```
aws ec2 describe-security-groups --filters Name=vpc-id,Values=vpc-XXXXXXXXX --region us-east-1
``` 

# add ingress rule to security group 
```
aws ec2 authorize-security-group-ingress --group-id sg-01302b1c9c719a4aa --protocol tcp --port 80 --cidr 0.0.0.0/0 --region us-east-1 
``` 

# deploy docker-compose file to cluster 
```
ecs-cli compose --project-name tutorial service up --create-log-groups --cluster-config tutorial
```
