import time
import machine
import http
import screen
import blink
import secrets


apiUrl = "http://api.lakitna.nl/?key=" + secrets.apikey

backlight = machine.Pin(4, machine.Pin.OUT)


print("Main.py");


backlight.high()
http.do_connect()
backlight.low()



while True:
	response = http.getJSON(apiUrl);
	print(str(response['time']['h']) + ':' + str(response['time']['m']))
	print(response);

	# http.updateJSON(apiUrl, '0:{"latest":{"y":2017,"m":6,"d":2},"next":{"y":2017,"m":9,"d":2}}')

	time.sleep(60);
