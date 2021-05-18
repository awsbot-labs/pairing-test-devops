# 101ways.awsbot.com
A dockerised, highly available, autoscaling nginx two node cluster running on AWS Elastic Container Services (ECS). 

The system should automatically provision the configured number of nginx containers. If an instance is terminated, 
or the docker image fails for some reasmon, the instance or containers will be automatically launched or restarted.

This architecture features:
* **Resiliency across 2 availability Zones**
* **Runs Nginx inside docker containers**
* Autoscaling groups
* A load-balancer
* Docker service management with ECS
* Ability to change the version number i.e. content of the index.html via CloudFormation parameters.

## Contents
* template.yaml
* main.py
* Makefile

### template.yaml
Cloudformation template for the infrastructure

### main.py
Python script to run health checks

### Makefile
Contains helpful commands for automatation and buildspecs. See the contents for more information.
  
## Instructions
### How to create the server
1. Run the command
```
    make create_cloudformation
```
2. Enter the aws `access_key_id`, and `secret_access_key`, and the other options requested by the `aws-cli`.
3. Go to CloudFormation in the AWS console to observe the stack creation.
4. Once complete open the "Outputs" tab and note the URL. This can be tested in a browser.

### How to run the health check script
1. Run the script with the following command:
```
    make health_check
```
2. You will be prompted for the URL to check. Otherwise you can set this manually.

**Note. Since this is an HA system, it is not necessary to restart the service tasks with the health script, although this can be done via boto3.**
 
# References
* ECS: https://docs.aws.amazon.com/ecs/index.html
* boto3: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html