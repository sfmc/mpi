#!/usr/bin/python
import time
import interfaces.gpio
import interfaces.servo_hat
import helpers.color_utilities
from helpers.button_listener import ButtonListener
from state_machine.startup_state import StartupState
from state_machine.idle_state import IdleState
from state_machine.entertain_state import EntertainState


class Robot():
	def button_click(self):
		self.state = self.state.button_click()

		
	def button_double_click(self):
		self.state = self.state.button_double_click()

		
	def button_long_press(self):
		self.state = self.state.button_long_press()

		
	def __init__(self):
		interfaces.gpio.initialize()
		interfaces.servo_hat.initialize()
		listener = ButtonListener(7, 1, self.button_click, self.button_double_click, self.button_long_press) 
		
		initial_state = StartupState()
		self.state = initial_state
		#self.state = EntertainState(True)
		time.sleep(2)
		# Note: we may have moved on if user pressed a button
		if (self.state == initial_state):
			self.state.stop()
			self.state = IdleState()
		
		while True:
			time.sleep(60)


if __name__ == "__main__":
	#interfaces.servo_hat.initialize()
	#interfaces.servo_hat.set_button_color_rgb(0,0,0)
	#interfaces.servo_hat.shutdown() # Note: should be before gpio.shutdown
	#interfaces.gpio.initialize()
	#interfaces.gpio.shutdown()
	Robot()
	#interfaces.servo_hat.initialize()
	#interfaces.servo_hat.set_laser_angles(0,0)