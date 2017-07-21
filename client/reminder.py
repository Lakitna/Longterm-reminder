from days import addMonth
from http import updateJSON
import settings



def defineActive(activeReminders, response):
	if response['next'] < settings.dayCountActive:
		if response['id'] not in activeReminders:
			activeReminders[ response['id'] ] = response
	else:
		if response['id'] in activeReminders:
			del activeReminders[ response['id'] ]

def setComplete(reminder):
	updateJSON( {str(reminder['id']): {'latest': settings.time.get_obj(), 'next': addMonth( settings.time.get_obj(), reminder['freq_month'] )}} )
	settings.HTTPupdateFlag = True
