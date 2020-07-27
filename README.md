![Seymore](https://github.com/outrun7/PlantPal/blob/master/seymore.jpg)

# PlantPal
A Raspberry Pi and Amazon Web Services project. Never let your plants go dry again! Receive an email from AWS Simple Notification Service (SNS) when your plants are running low on water. When the moisture sensor detects a change (plant is dry), the pi will publish a message in AWS SNS, which will send an email to the defined inbox. 
![email](https://github.com/outrun7/PlantPal/blob/master/email.PNG)

## Hardware

- [Moisture Sensor](https://www.amazon.com/gp/product/B071F4RDHY/)
  - [Setup moisture sensor](https://www.instructables.com/id/Soil-Moisture-Sensor-Raspberry-Pi/)
- [Raspberry Pi](https://www.amazon.com/ELEMENT-Element14-Raspberry-Pi-Motherboard/dp/B07P4LSDYV) You can use any pi for this project 
- Seymore the Brave Test Plant  

Get the moisture sensor, pi, and brave test plant all plugged in. 

## Download the code
    git clone https://github.com/outrun7/PlantPal.git
   
## Install dependencies
    pip3 install boto3
    
## Create an SNS topic 
[SNS documentation](https://docs.aws.amazon.com/sns/latest/dg/sns-tutorial-create-topic.html)

Create an email subscription to the topic. 

I chose to encrypt my messages server-side and kept publishing and reading restricted to topic owner (my account). 

![SNS Topic](https://github.com/outrun7/PlantPal/blob/master/snsTopic.PNG)

## Setup IAM
Log into a non-root AWS account and create an IAM user with programatic access only.

Create a policy that allows SNS Publish only. 

Attach the policy to the user you've created for PlantPal. 

Example policy. Note the ARN will be for the SNS topic created above:
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
````

![PlantPal User](IAMPlantPalUser.PNG)

## Storing access keys securely and working with Boto3
[Generate a secure access key for your PlantPal user in the IAM console](https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html) and place the key in the ~/.aws/credentials file. Boto3 will look here and use this key to auth to AWS. 

your ~/.aws/credentials file will look like this: 
````
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
````

Also ensure your ~/.aws/config file has the region info filled out. It should look something like this: 
````
[default]
region = us-east-1
output=
````

[How Boto3 handles credentials](https://boto3.amazonaws.com/v1/documentation/api/1.9.46/guide/configuration.html)  

The mechanism in which Boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

- Passing credentials as parameters in the boto.client() method
- Passing credentials as parameters when creating a session object
- Environment variables
- Shared credential file (~/.aws/credentials)   **<- We're using this**
- AWS config file (~/.aws/config)
- Assume Role provider
- Boto2 config file (/etc/boto.cfg and ~/.boto)
- Instance metadata service on an Amazon EC2 instance that has an IAM role configured

## Setup a Cron Watchdog
    crontab -e 
    
Enter the following line to ensure our watchdog script runs every 15 minutes. (We wouldn't want our plants getting thirsty, would we?!)

    */15 * * * * ~/PlantPal/checkIfRunning.sh
    
## Enjoy your happy plants 
![happy plant](https://media2.giphy.com/media/ZNn2OLYWJYDC60OKuo/giphy.gif?cid=ecf05e47ujyv884o0b04799z8a9qbjb2t2e8ezh1ryp1qbss&rid=giphy.gif)

## To do
- export this in CF or other Infrastructure as Code template.

