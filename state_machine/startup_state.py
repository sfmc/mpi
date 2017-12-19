#!/usr/bin/python
import time, threading
import helpers.color_utilities
from robot_state import RobotState
from idle_state import IdleState
from shutdown_state import ShutdownState


class StartupState(RobotState):
	def __init__(self):
		self.stop_event = threading.Event()
		self.t1 = threading.Thread(target=self.run)
		self.t1.setDaemon(True)
		self.t1.start()


	def run(self):
		while (self.stop_event.is_set() == False):
			helpers.color_utilities.glow(helpers.color_utilities.WHITE, 1)
		return


	def stop(self):
		self.stop_event.set()
		self.t1.join()
			
	
	def button_click(self):
		self.stop()
		return IdleState()
	
	
	def button_double_click(self):
		self.stop()
		return IdleState()
	
	
	def button_long_press(self):
		self.stop()
		return ShutdownState()