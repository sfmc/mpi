#!/usr/bin/python
import time, threading
import RPi.GPIO as GPIO

class ButtonListener:
	debounce_time = 0.05
	long_press_duration = 2
	double_click_interval = 0.4
	

	def poll_loop(self):
		button_pressed = False
		button_down_time = 0.0
		button_up_time = 0.0
		last_click_time = 0.0
		ignore_next_button_up_transition = False
		
		while True:
			time.sleep(0.05) # 20Hz
			sample_time = time.time()
			sample_pressed = (GPIO.input(self.pin_number) == self.pressed_value)

			# Update button state
			button_down_transition = sample_pressed and not button_pressed
			button_up_transition = not sample_pressed and button_pressed
			if (button_down_transition):
				button_down_time = sample_time
				time.sleep(ButtonListener.debounce_time)
			elif (button_up_transition):
				button_up_time = sample_time
				time.sleep(ButtonListener.debounce_time)
			
			# Check for long press
			button_press_duration = sample_time - button_down_time
			if (sample_pressed and (button_press_duration > ButtonListener.long_press_duration)):
				self.long_press()
			# Check for double click
			elif (button_down_transition):
				time_between_clicks = sample_time - last_click_time
				if (time_between_clicks < ButtonListener.double_click_interval):
					last_click_time = 0.0 # Prevent multiple double clicks in a row
					self.double_click()
					ignore_next_button_up_transition = True
			# Check for click
			elif (button_up_transition):
				if (not ignore_next_button_up_transition):
					last_click_time = sample_time
				ignore_next_button_up_transition = False
			# Click, but not double click
			else:
				time_since_click = sample_time - last_click_time
				if (time_since_click > ButtonListener.double_click_interval and time_since_click < (2 * ButtonListener.double_click_interval)):
					last_click_time = 0.0 # Prevent multiple clicks in a row
					self.click()
			# Update button state
			button_pressed = sample_pressed			


	def __init__(self, pin_number, pressed_value, click, double_click, long_press):
		self.pin_number = pin_number
		self.pressed_value = pressed_value
		self.click = click
		self.double_click = double_click
		self.long_press = long_press
		t1 = threading.Thread(target=self.poll_loop)
		t1.setDaemon(True)
		t1.start()
		return