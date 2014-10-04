#!/usr/local/bin/python2.7

## raspi-alarm.py -- for waking up
## Created by furiousmonkey
## Last Updated 4-Oct-2014 updated 4 times

import sched
import time
import os
from datetime import datetime, timedelta
alarm_time = addSecs(datetime.now().isoformat(), 15) # for testing.
#alarm_sound = '/var/mp3/alarm/mp3'

def checkTime():
  check_now = datetime.now().isoformat()
  if check_now == alarm_time:
    print startAlarm()
  return check_now
    
def startAlarm():
  # used to start the audio, take the PIN, and either snooze or stop the alarm.
  #alarm_sound.play()
  date_code = datetime.now().strftime('%d%m%y')
  stop_code = raw_input('Today\'s Date')
  if stop_code == date_code:
    #alarm_sound.stop()
    return 'Good morning!'
  else:
    #alarm_sound.snooze()
    alarm_time = addSecs(alarm_time, 600) 
  return 'You lazy son-of-a...'
  
def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()
	
	
'''
Input: USB Number Pad
Output: 1 x Speaker
'''
