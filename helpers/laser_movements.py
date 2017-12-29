#!/usr/bin/python
import math, time
import interfaces.servo_hat
import helpers.utilities

def draw_circle():
	for a in helpers.utilities.drange(0, 6.28, 0.1):
		time.sleep(0.05)
		pan = 60*math.sin(a)
		tilt = 60*math.cos(a)
		interfaces.servo_hat.set_laser_angles(pan,tilt)
	#return
	#interfaces.servo_hat.set_laser_angles(50,0)
	#time.sleep(0.5)
	#interfaces.servo_hat.set_laser_angles(0,0)
	#time.sleep(0.5)
	#interfaces.servo_hat.set_laser_angles(-50,0)
	#time.sleep(0.5)
	#interfaces.servo_hat.set_laser_angles(0,0)
	

