#!/usr/bin/python
import time, threading
import helpers.color_utilities
import helpers.laser_movements
import interfaces.servo_hat
import robot_state
import idle_state
import shutdown_state


class EntertainState(robot_state.RobotState):
	def __init__(self, record):
		self.stop_event = threading.Event()
		self.glow_color = helpers.color_utilities.RED if record else helpers.color_utilities.GREEN
		self.t1 = threading.Thread(target=self.run)
		self.t1.setDaemon(True)
		self.t1.start()
		
	
	def run(self):
		helpers.color_utilities.set_button_color(self.glow_color)
		interfaces.servo_hat.laser_on()
		while (self.stop_event.is_set() == False):
			#helpers.color_utilities.glow(self.glow_color, 1)
			helpers.laser_movements.draw_circle()
			time.sleep(0.05)
		interfaces.servo_hat.laser_off()
		return

		
	def stop(self):
		self.stop_event.set()
		self.t1.join()
		
		
	def button_click(self):
		self.stop()
		return idle_state.IdleState()

		
	def button_double_click(self):
		self.stop()
		return idle_state.IdleState()

		
	def button_long_press(self):
		self.stop()
		return shutdown_state.ShutdownState()