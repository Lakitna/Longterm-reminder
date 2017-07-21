import settings
import http
import days
import reminder

activeReminders = {}

def do():
	time = settings.time
	settings.HTTPupdateFlag = False

	# Retrieve data
	response = http.getJSON()
	print()
	print(response);

	# Set TimeKeeper to server time
	time.set(response['now']['Y'], response['now']['M'], response['now']['D'], response['now']['h'], response['now']['m'])
	# Remove server time from response
	response = response['content']

	# Iterate every reminder
	for i in range(0, len(response)):
		# Simplify response: 'next' in days instead of date
		dayCount = days.dateToDays(time.get_obj(), response[str(i)]['next'])
		response[str(i)]['next'] = dayCount

		if dayCount < -1000: # If 'next' date is unset
			reminder.setComplete( response[str(i)] )

		# Define active reminders
		reminder.defineActive( activeReminders, response[str(i)] )

	return response
