# PlantPal
Write up and code for my Plant Pal project to learn IAM and SNS 


Storing Access Keys Securely
https://boto3.amazonaws.com/v1/documentation/api/1.9.46/guide/configuration.html
The mechanism in which boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

Passing credentials as parameters in the boto.client() method
Passing credentials as parameters when creating a Session object
Environment variables
Shared credential file (~/.aws/credentials)
AWS config file (~/.aws/config)
Assume Role provider
Boto2 config file (/etc/boto.cfg and ~/.boto)
Instance metadata service on an Amazon EC2 instance that has an IAM role configured.
Each of those locations is discussed in more detail below.
