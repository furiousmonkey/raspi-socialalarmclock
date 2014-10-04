#!/usr/local/bin/python2.7

## raspi-alarm.py -- for waking up
## Created by furiousmonkey
## Last Updated 4-Oct-2014

import sched
import time
import os
import RasPi.GPIO as GPIO
from datetime import datetime, timedelta

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


global alarm_hour, alarm_minute, alarm_mp3
parser = SafeConfigParser()
parser.read('rpi_alarm.cfg')

alarm_hour = parser.get('options', 'hour')
alarm_minute = parser.get('options', 'minute')
alarm_mp3 = parser.get('options', 'mp3')

def checkTime():
  check_now = "$s:$s" % (datetime.now().hour, datetime.now().minute)
  if check_now == alarm_time:
    print startAlarm()
  return check_now
    
def startAlarm():
  # used to start the audio, take the PIN, and either snooze or stop the alarm.
  alarm_sound.play()
  date_code = datetime.now().strftime("%d%m%y")
  stop_code = raw_input("Today\'s Date")
  if stop_code == date_code:
    alarm_sound.stop()
    return "Good morning!"
  else:
    alarm_sound.snooze()
    alarm_time = addSecs(alarm_time, 600) 
  return "You lazy son-of-a..."
  
  def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()
	
	
"""
Input: USB Number Pad
Output: 1 x LED, 1 x Speaker
"""
