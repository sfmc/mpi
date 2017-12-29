#!/usr/bin/python
import math, time
import interfaces.servo_hat
import helpers.utilities

def draw_circle():
	time_step = 0.005
	pan_period = 3
	tilt_period = 1
	pan_steps_per_period = pan_period / time_step
	tilt_steps_per_period = tilt_period / time_step
	for i in range(0, int(pan_steps_per_period)):
		pan_angle = 6.282 * i / pan_steps_per_period
		tilt_angle = 6.282 * i / tilt_steps_per_period
		pan = 120*math.sin(pan_angle)
		tilt = 10+10*math.cos(tilt_angle)
		interfaces.servo_hat.set_laser_angles(pan,tilt)
		time.sleep(time_step)