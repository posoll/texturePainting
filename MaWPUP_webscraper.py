import urllib2
import time
from twilio.rest import Client

account_sid = 'XXX'
auth_token = 'XXX'
twilio_phone_number = '+XXX'
my_phone_number = '+XXX'

def WebData():
	
	link = raw_input("Paste URL here:")
	sec = int(raw_input("How many seconds do you want to test for? If you would like to run until a change is detected enter 0."))
	
	URL = urllib2.urlopen(link)
	data = URL.read()
	datastring = str(data)
	lengthB = len(datastring)
	
	timeT = 0
	
	if sec == 0:
		while True:
	
			URL = urllib2.urlopen(link)
			data = URL.read()
			datastring = str(data)
			lengthA = len(datastring)
		
			print "Testing..."
			if lengthB != lengthA:
				print "The site has changed!"
				body = "The price has changed!"
				client = Client(account_sid, auth_token)
				client.messages.create(
					body=body,
					to=my_phone_number,
					from_=twilio_phone_number
				)
				break
			else:
				lengthA = lengthB
				timeT += 1
				time.sleep(1)
		
	else:
		while timeT < sec:
	
			URL = urllib2.urlopen(link)
			data = URL.read()
			datastring = str(data)
			lengthA = len(datastring)
		
			print "Testing..."
			if lengthB != lengthA:
				print "The site has changed!"
				body = "The price has changed!"
				client = Client(account_sid, auth_token)
				client.messages.create(
					body=body,
					to=my_phone_number,
					from_=twilio_phone_number
				)
				break
			else:
				lengthA = lengthB
				timeT += 1
				time.sleep(1)
			
			if timeT == sec:
				print "No changes were made."
	
WebData()