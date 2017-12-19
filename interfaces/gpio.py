#!/usr/bin/python
import RPi.GPIO as GPIO

def initialize():
	print 'initialize'
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(26, GPIO.IN)
	#GPIO.setup(11, GPIO.OUT)
	#GPIO.output(11, 0) # 0 so we button press => Pin5 connected to Groud(Pin11)
	return

	
def shutdown():
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(11, GPIO.OUT)
	#GPIO.output(11, 1) # 0 so we button press => Pin5 connected to Groud(Pin11)
	
	return
	#print 'shutdown'
	#GPIO.setmode(GPIO.BOARD)
	#GPIO.setup(7, GPIO.OUT)
	#GPIO.output(7, 0) # 0 so we button press => Pin5 connected to Groud(Pin7)
	
	#GPIO.setup(11, GPIO.OUT)
	#GPIO.output(11, 0) # 0 so we button press => Pin5 connected to Groud(Pin7)