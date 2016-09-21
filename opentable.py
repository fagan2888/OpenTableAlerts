from bs4 import BeautifulSoup
import requests
#Dependencies - requests, beautifulsoup4, lxml

# Date and time you want to search
date = '2016-09-02 19:00'

#Restaruant ID goes below
url="http://www.opentable.com/restaurant/profile/152023/search"
flare_url = "https://maker.ifttt.com/trigger/"YOUR EVENT"/with/key/"YOUR KEY""


def search():
	response = requests.post(url, json={"covers": "2", "dateTime": date})
	page_data = BeautifulSoup(response.text, "lxml")
	times = page_data.findAll('a', class_="dtp-button button")
	times_list = []

	#This is a dumb way to do times, I know, but its also easy and extremely lazy
	for item in times:
		times_list.append(item.get_text())
	if "5:45 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "545PM"})
	if "6:00 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "6PM"})
	if "6:15 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "615PM"})
	if "6:30 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "630PM"})
	if "6:45 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "645PM"})
	if "7:00 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "7PM"})
	if "7:15 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "715PM"})
	if "7:30 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "735PM"})
	if "7:45 PM" in times_list:
		flare = requests.post(flare_url, data={"value1": "745PM"})

search()