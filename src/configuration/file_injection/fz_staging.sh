#!/bin/bash
export AWS_PROFILE=default
bastion_id=$(aws ec2 describe-instances --filters "Name=tag:Name,Values=adad-ec2-bastion" --query "Reservations[].Instances[?State.Name=='running'].InstanceId" --output text --region eu-west-3)

aws ssm start-session --target $bastion_id  --region eu-west-3 --document-name AWS-StartPortForwardingSessionToRemoteHost --parameters '{"portNumber":["2022"],"localPortNumber":["4445"],"host":["15.236.129.45"]}'
