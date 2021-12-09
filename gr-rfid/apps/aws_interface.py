from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json
import time
import os

w_dir = os.getcwd().split("HealthX")[0] + "HealthX"

set_serve = False
host = "a39nu1xs62gahx-ats.iot.us-east-1.amazonaws.com"
certPath = w_dir + "/cert/"
clientId = "pizerow"
topic = "location"
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = None
myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)

#print (hr)
def setup():
	# Init AWSIoTMQTTClient
	#myAWSIoTMQTTClient = None
	#myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
	myAWSIoTMQTTClient.configureEndpoint(host, 8883)
	myAWSIoTMQTTClient.configureCredentials("{}RootCA1.pem".format(certPath), "{}Rpi-private.pem.key".format(certPath), "{}Rpi-cert.pem.crt".format(certPath))

	# AWSIoTMQTTClient connection configuration
	myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
	myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
	myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
	myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
	myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
	myAWSIoTMQTTClient.connect()

	set_serve = True

# setup()
def push(pat_id, loc):
	if not set_serve:
		setup()
	
	#id='1876'
	messageJson = json.dumps({"ID": pat_id, "location": loc})
	myAWSIoTMQTTClient.publish(topic, messageJson, 1)
	print('Published topic %s: %s\n' % (topic, messageJson))
	time.sleep(1)
#myAWSIoTMQTTClient.disconnect()
