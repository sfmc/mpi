#!/usr/bin/python
import math, time
import interfaces.servo_hat
import helpers.utilities

def draw_circle():
	time.sleep(0.5)
	interfaces.servo_hat.set_laser_angles(50,0)
	time.sleep(0.5)
	interfaces.servo_hat.set_laser_angles(0,0)
	time.sleep(0.5)
	interfaces.servo_hat.set_laser_angles(-50,0)
	time.sleep(0.5)
	interfaces.servo_hat.set_laser_angles(0,0)
	
	

