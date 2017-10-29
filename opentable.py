import requests
import os

def run(event, context):
	opentable_rid = os.environ['opentable_rid']
	date = os.environ['date']
	#ifttt_key = os.environ['ifttt_key']
	#event_id = os.environ['event_id']
	people = os.environ['people']
	url = "https://www.opentable.com/restaurant/profile/%s/search" % (opentable_rid)
	response = requests.post(url, json={"covers": people, "dateTime": date})
	times_list = ["5:45 PM", "6:00 PM", "6:15 PM", "6:30 PM", "6:45 PM", "7:00 PM", "7:15 PM", "7:30 PM", "7:45 PM"]
	fail_message = "No tables are available"
	for time in times_list:
		if fail_message in response.text:
			print "No Tables"
			return
		else:
			if time in response.text:
				print time
				#flare = requests.post(flare_url, data={"value1": "545PM"})