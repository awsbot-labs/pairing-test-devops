PROFILE:=awsbot
STACK_NAME:=com-awsbot-101ways

# Runs the health check script
health_check:
	@python main.py

# Creates the system with CloudFormation
create_cloudformation:
	unset AWS_DEFAULT_REGION; \
	aws configure --profile $(PROFILE); \
	aws cloudformation create-stack \
		--profile $(PROFILE) \
		--stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_IAM \
		--template-body file://template.yaml

# Updates the system once created in cloudformation
update_cloudformation:
	unset AWS_DEFAULT_REGION; \
	aws configure --profile $(PROFILE); \
	aws cloudformation update-stack \
		--profile $(PROFILE) \
		--stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_IAM \
		--template-body file://template.yaml