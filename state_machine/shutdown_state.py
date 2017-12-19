#!/usr/bin/python
import os
import helpers.color_utilities
import interfaces.gpio
import interfaces.servo_hat
from robot_state import RobotState


class ShutdownState(RobotState):
	def __init__(self):
		helpers.color_utilities.glow(helpers.color_utilities.ORANGE, 2)
		helpers.color_utilities.glow(helpers.color_utilities.ORANGE, 2)
		helpers.color_utilities.glow(helpers.color_utilities.ORANGE, 2)
		helpers.color_utilities.glow(helpers.color_utilities.BLACK, 2)
		interfaces.servo_hat.shutdown() # Note: should be before gpio.shutdown
		interfaces.gpio.shutdown()
		os.system('poweroff')
		
	def button_click(self):
		return self

		
	def button_double_click(self):
		return self

		
	def button_long_press(self):
		return self