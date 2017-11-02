import requests
import os
import boto3

def run(event, context):
	opentable_rid = os.environ['opentable_rid']
	date = os.environ['date']
	ifttt_key = os.environ['ifttt_key']
	ifttt_id = os.environ['ifttt_id']
	people = os.environ['people']
	url = "https://www.opentable.com/restaurant/profile/%s/search" % (opentable_rid)
	ifttt_url = "https://maker.ifttt.com/trigger/%s/with/key/%s" % (ifttt_id, ifttt_key)
	response = requests.post(url, json={"covers": people, "dateTime": date})
	times_list = ["5:45 PM", "6:00 PM", "6:15 PM", "6:30 PM", "6:45 PM", "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM"]
	fail_message = "No tables are available"
	success_flag = False
	for time in times_list:
		if fail_message in response.text:
			print "No Reservations Available"
			return
		else:
			if time in response.text:
				print time
				alert = requests.post(ifttt_url, data={"value1": time})
				success_flag = True
	if success_flag == True:
		client = boto3.client('events')
		response = client.disable_rule(Name='OpenTableAlerts')
		return "Disabled Lambda function to prevent spam"