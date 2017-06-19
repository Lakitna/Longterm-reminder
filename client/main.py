import time
import machine
import http
# import screen
import blink
import secrets

apiUrl = "http://api.lakitna.nl/?key=" + secrets.apikey + "&src=mpy"


http.do_connect()

while True:
	response = http.getJSON(apiUrl);
	print()
	print(str(response['now']['Y']) + '-' + str(response['now']['M']) + '-' + str(response['now']['D']) + ' ' + str(response['now']['h']) + ':' + str(response['now']['m']))
	print(response);

	# http.updateJSON(apiUrl, '0:{"latest":{"y":2017,"m":6,"d":2},"next":{"y":2017,"m":9,"d":2}}')

	time.sleep(60);
