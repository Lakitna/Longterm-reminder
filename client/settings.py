import secrets
from delay import Delay
from timekeeper import TimeKeeper


time = TimeKeeper(0,0,0,0,0)

dayCountActive = 7		# Max days left before reminder becomes active
ldrMinValue = 5 		# LDR value under which screen turns off [0-1023]

HTTPupdateDelay = Delay(10 * 60 * 1000) # delay time in milliseconds
screenUpdateDelay = Delay(1 * 1000)		# delay time in milliseconds
apiUrl = "http://api.lakitna.nl/?src=upy&key=" + secrets.apikey # URL to API

HTTPupdateFlag = True
