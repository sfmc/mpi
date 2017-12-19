#!/usr/bin/python

class RobotState():
	def __init__(self):
		pass
	
	def stop(self):
		pass
	
	def button_click(self):
		return self
	
	def button_double_click(self):
		return self
	
	def button_long_press(self):
		return self
	
	def __repr__(self):
		return self.__str__()

	def __str__(self):
		return self.__class__.__name__