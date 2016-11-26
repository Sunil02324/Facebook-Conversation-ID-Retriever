import requests
import json
from time import sleep

http_proxy  = "http://10.3.100.207:8080"
https_proxy = "https://10.3.100.207:8080"
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
              }


url = '###'

threadid = 0

userId = ####

first = True
loop = True
while loop:
	try:
		resp = requests.get(url,proxies=proxyDict)
		if first:
			data = resp.json()
			for thread in data['data']:
				if thread['to']['data'][0]['id'] == str(userId):
					threadid = int(thread['id'])
					loop = False
					break
			url = data['paging']['next']
			first = False
		else:
			data1 = resp.json()
			try:
				if(data1['data']):
					for thread in data1['data']:
						if thread['to']['data'][0]['id'] == str(userId):
							threadid = int(thread['id'])
							loop = False
							break
					url = data1['paging']['next']
				else:
					loop = False
			except:
			    print "Response does not contain 'data', here is what Response looks like:"
			    sleep(20)
	except IOError as e:
		print "Socket error. Sleeping for 5 seconds"
		sleep(2)
		continue
	except requests.exceptions.ConnectionError as e:
		print "Proxy Error. Stopping the script for 5 seconds"
		sleep(2)
		continue

print "The Required Thread Id is " + str(threadid)