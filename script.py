import requests
import json
from time import sleep

http_proxy  = "http://10.3.100.207:8080"
https_proxy = "https://10.3.100.207:8080"
proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy
              }


#Replace <access_token> with your access token from https://developers.facebook.com/tools/explorer/145634995501895?method=GET&path=me%2Finbox&version=v2.2
url = 'https://graph.facebook.com/v2.2/me/inbox?access_token=<access_token>'

threadid = 0

# User ID/Profile ID of the person
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

print "The Required Conversation Id is " + str(threadid)