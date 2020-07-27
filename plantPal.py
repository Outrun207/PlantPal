#!/usr/bin/python3

#store your creds in ~/.aws/credentials and setup your ~/.aws/config file with proper region. 

import RPi.GPIO as GPIO 
import smtplib 
import time 
import boto3

#sns publish message
#make an sns client with boto3
snsClient = boto3.client('sns')
#make and publish a message to sns topic
sendMessage = snsClient.publish(
#change me
TopicArn = 'arn:aws:sns:<region>:<topic id>',
#change me
Message = 'The <plant> in the <room> may be thirsty. Please check and water.',
)

#detect GIPO changes. The hydrometer/GIPO is good at measuring changes to state, but wasn't accurately detecting whether dry or wet. We'll just detect if a state changed. 

def callback(channel):  
	if GPIO.input(channel):
		sendMessage
		#print("change detected")

	else:
		sendMessage
		#print("change detected")


# Set GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin 
channel = 23
# Set GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

# This is an infinte loop to keep our script running
while True:
	#sleepy time (save processor) 
	time.sleep(0.1)
