<a href="https://github.com/outrun7/PlantPal/blob/master/seymore.jpg"><img src="https://github.com/outrun7/PlantPal/blob/master/seymore.jpg" align="left" height="100" width="120" ></a>
# PlantPal
A Raspberry Pi and Amazon Web Services project. Never let your plants go dry again! Receive an email from AWS Simple Notification Service (SNS) when your plants are running low on water. 

## Hardware

- [Moisture Sensor](https://www.amazon.com/gp/product/B071F4RDHY/)
- [Raspberry Pi](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV) You can use any pi for this project 
- Seymore the Brave Test Plant  

## Download the code
    git clone https://github.com/outrun7/PlantPal.git
   
## Install dependencies
    pip3 install boto3
    
## Create an SNS topic 


## Setup IAM
Assuming you are following best practices, log into a non-root AWS account and creat an IAM user with programatic access only.

Create a policy that allows SNS Publish only. 

Attach the policy to the user you've created for Plant Pal. 

Example policy. Note the ARN will be for the SNS topic create above:
````{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:us-east-1:12345678910:Plant-Pal"    
        }
    ]

## Storing Access Keys Securely

[How boto3 handles credentials](https://boto3.amazonaws.com/v1/documentation/api/1.9.46/guide/configuration.html)  

The mechanism in which boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which boto3 searches for credentials is:

- Passing credentials as parameters in the boto.client() method
- Passing credentials as parameters when creating a Session object
- Environment variables
- Shared credential file (~/.aws/credentials)
- AWS config file (~/.aws/config)
- Assume Role provider
- Boto2 config file (/etc/boto.cfg and ~/.boto)
- Instance metadata service on an Amazon EC2 instance that has an IAM role configured
