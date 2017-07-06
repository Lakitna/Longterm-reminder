# Classes & backend
from secrets import apikey
from delay import Delay
from timekeeper import TimeKeeper
from screen import Screen
import http
import days

# Script extention
import inputs


# Global settings
##################
set_dayCountActive = 7		# Max days left before reminder becomes active
set_ldrMinValue = 1		# LDR value under which screen turns off [0-1023]

HTTPupdateDelay = Delay(10 * 60 * 1000) # delay time in milliseconds
screenUpdateDelay = Delay(1 * 1000)		# delay time in milliseconds
apiUrl = "http://api.lakitna.nl/?key=" + apikey + "&src=upy"  # URL to API


# Empty var declaration
########################
activeReminders = []
HTTPupdateFlag = True
currentIcon = 0


# Start setup
##############
oled = Screen()
displaySleep = False

# Connect to WiFi
oled.icon('wifi', 48, 10)
oled.text("Connecting", 24, 44, True)
oled.show()
http.do_connect()
oled.clear()
oled.icon('wifi', 48, 10)
oled.text("Success", 36, 44, True)
oled.show()
screenUpdateDelay.sleep()

time = TimeKeeper(0,0,0,0,0)


# Start loop
#############
while True:
	time.poll();
	inputs.poll();
	oled.fpsPoll();

	# On interval or on HTTPupdateFlag
	if HTTPupdateDelay.noSleep() or HTTPupdateFlag:
		HTTPupdateFlag = False

		response = http.getJSON(apiUrl)

		print()
		print(response);

		# Set TimeKeeper to server time
		time.set(response['now']['Y'], response['now']['M'], response['now']['D'], response['now']['h'], response['now']['m'])

		# Remove server time from response to make things more managable
		response = response['content']

		# Iterate every reminder
		for i in range(0, len(response)):
			# Simplify response: 'next' in days instead of date
			dayCount = days.dateToDays(time.get_obj(), response[str(i)]['next'])
			response[str(i)]['next'] = dayCount

			if dayCount < -1000: # If 'next' date is unset
				# Update 'latest' and 'next'
				next = days.addMonth( time.get_obj(), response[str(i)]['freq_month'] )
				http.updateJSON(apiUrl, {str(i): {'latest': time.get_obj(), 'next': next}})

				HTTPupdateFlag = True # Rerun HTTPupdate routine

			# Define active reminders
			if dayCount < set_dayCountActive:
				if i not in activeReminders:
					activeReminders.append(i)
			else:
				if i in activeReminders:
					activeReminders.remove(i)

			print(len(activeReminders))


	# Clear display
	oled.clear()

	# Build display
	if len(activeReminders) == 0:
		# Set display sleep state
		oled.sleep(True)
	else:
		# Set display sleep state
		if inputs.ldr_A.val_period < set_ldrMinValue:
			oled.sleep(True)
		else:
			oled.sleep(False)

		# Different screens for different amount of active reminders
		if len(activeReminders) == 1:
			descr = response[str(activeReminders[0])]['descr']
			oled.icon(response[str(activeReminders[0])]['icon'], 48, 0)
			oled.text(descr, (64 - ( len(descr) * 4 )), 36) # Center aligned

		elif len(activeReminders) == 2:
			descr = response[str(activeReminders[0])]['descr']
			oled.icon(response[str(activeReminders[0])]['icon'], 16, 0)
			oled.text(descr, (32 - ( len(descr) * 4 )), 36) # Center aligned

			oled.line(64,0, 64,64)

			descr = response[str(activeReminders[1])]['descr']
			oled.icon(response[str(activeReminders[1])]['icon'], 80, 0)
			oled.text(descr, (96 - ( len(descr) * 4 )), 36) # Center aligned


		oled.text(str(oled.fps), 0, 56)
		if inputs.but_A.val == 1:
			oled.rect(107, 62, 10, 2)
		if inputs.but_B.val == 1:
			oled.rect(118, 62, 10, 2)

		oled.show()



		# oled.clear()
		# oled.text('%s' % displayText, 0, 0)
		# oled.icon(currentIcon, 96, 0)
		# oled.text(str(oled.fps), 0, 50)
