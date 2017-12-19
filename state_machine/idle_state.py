#!/usr/bin/python
import time, threading
import helpers.color_utilities
from robot_state import RobotState
from entertain_state import EntertainState
from shutdown_state import ShutdownState


class IdleState(RobotState):
	def __init__(self):
		helpers.color_utilities.set_button_color(helpers.color_utilities.WHITE, 0.5)
		self.stop_event = threading.Event()
		self.t1 = threading.Thread(target=self.run)
		self.t1.setDaemon(True)
		self.t1.start()


	def run(self):
		while (self.stop_event.is_set() == False):
			time.sleep(0.05)
		return

		
	def stop(self):
		self.stop_event.set()
		self.t1.join()
	
	
	def button_click(self):
		self.stop()
		return EntertainState(False)
	
	
	def button_double_click(self):
		self.stop()
		return EntertainState(True)
	
	
	def button_long_press(self):
		self.stop()
		return ShutdownState()