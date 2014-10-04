#!/usr/local/bin/python2.7

## raspi-alarm.py -- for waking up
## Created by furiousmonkey
## Last Updated 4-Oct-2014 updated 4 times

import sched
import time
import os
from datetime import datetime, timedelta

global alarm_time

#alarm_sound = '/var/mp3/alarm/mp3'

def checkTime():
	while True:
		time.sleep(1)
		check_now = datetime.now().strftime("%H:%M:%S")
		if check_now == alarm_time.strftime("%H:%M:%S"):
			if checkCode():
				print "Good morning!"
				break
			else:
				print 'You lazy son-of-a...'
		else:
			print check_now

def checkCode():
	# used to start the audio, take the PIN, and either snooze or stop the alarm.
	#alarm_sound.play()
	global alarm_time
	date_code = datetime.now().strftime('%d%m%y')
	stop_code = raw_input('Today\'s Date: ')
	if stop_code == date_code:
		#alarm_sound.stop()
		return True
	else:
		#alarm_sound.snooze()
		alarm_time = addSecs(alarm_time, 10)
		return False
		

def addSecs(tm, secs):
    fulldate = datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + timedelta(seconds=secs)
    return fulldate.time()

alarm_time = addSecs(datetime.now(), 10) # for testing.

checkTime()

'''
Input: USB Number Pad
Output: 1 x Speaker
'''