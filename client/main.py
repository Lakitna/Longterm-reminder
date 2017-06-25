# Classes & backend
from secrets import apikey
from delay import Delay
from timekeeper import TimeKeeper
import http

# Script extention
import inputs
# import screen


# Global settings
HTTPupdateDelay = Delay(10 * 60 * 1000) # delay time in milliseconds
apiUrl = "http://api.lakitna.nl/?key=" + apikey + "&src=mpy"


# Empty var declaration


# Start setup
http.do_connect()
time = TimeKeeper(0,0,0,0,0)


# Start loop
while True:
	inputs.poll();
	time.poll();

	# If interval passed or on first loop
	if HTTPupdateDelay.noSleep():
		response = http.getJSON(apiUrl);
		print()
		print(response);

		# Set TimeKeeper to server time
		time.set(response['now']['Y'], response['now']['M'], response['now']['D'], response['now']['h'], response['now']['m'])
		print(time.get_stamp())

		# Works
		# http.updateJSON(apiUrl, '{"0":{"latest":{"y":2017,"m":6,"d":2},"next":{"y":2017,"m":9,"d":2}}}')
