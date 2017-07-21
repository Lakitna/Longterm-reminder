# Classes & backend
from secrets import apikey
import screen
from http import wifi_connect

# Script extention
import inputs
import httpUpdate

# Global settings
import settings


# Empty var declaration
########################

# Start setup
##############
displaySleep = False

# Connect to WiFi
screen.statusShow(0) # Connecting...
wifi_connect()
screen.statusShow(1) # Success
# Wait a bit
settings.screenUpdateDelay.sleep()

# Start loop
#############
while True:
	settings.time.poll();
	inputs.poll();

	# Update on interval or on HTTPupdateFlag
	if settings.HTTPupdateDelay.noSleep() or settings.HTTPupdateFlag:
		response = httpUpdate.do()
		# print(settings.time.get_obj())

	screen.build( response )
