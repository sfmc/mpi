#!/usr/bin/python
import smbus
import helpers.utilities 

# https://learn.sparkfun.com/tutorials/pi-servo-hat-hookup-guide
# https://github.com/sparkfun/Pi_Servo_Hat/blob/master/Examples/example.py

# Hardware Addresses
PAN_START = 0x06		# Ch0 = Pan
PAN_STOP = 0x08
TILT_START = 0x0A		# Ch1 = Tilt
TILT_STOP = 0x0C
LED_R_START = 0x16  	# Ch4 = LED Red
LED_R_STOP = 0x18
LED_G_START = 0x1A  	# Ch5 = LED Green
LED_G_STOP = 0x1C
LED_B_START = 0x1E  	# Ch6 = LED Blue
LED_B_STOP = 0x20
LASER_START = 0x26  	# Ch8 = Laser
LASER_STOP = 0x28

# Motor Calibration
PAN_CALIB_MIN = 836
PAN_CALIB_MAX = 1664
PAN_CALIB_DEGREES_RANGE = 180
TILT_CALIB_MIN = 836
TILT_CALIB_MAX = 1664
TILT_CALIB_DEGREES_RANGE = 180


def angle_to_pulse(angle, calib_min, calib_max, calib_degrees_range):
	midpoint = calib_min + (calib_max-calib_min) / 2
	ticks = midpoint + angle * (calib_max - calib_min) / calib_degrees_range
	ticks = int(round(helpers.utilities.clamp(ticks, calib_min, calib_max)))
	return ticks


def set_laser_angles(pan, tilt):
	pan_ticks = angle_to_pulse(pan, PAN_CALIB_MIN, PAN_CALIB_MAX, PAN_CALIB_DEGREES_RANGE)
	tilt_ticks = angle_to_pulse(tilt, TILT_CALIB_MIN, TILT_CALIB_MAX, TILT_CALIB_DEGREES_RANGE)
	bus.write_word_data(addr, PAN_STOP, pan_ticks)
	bus.write_word_data(addr, TILT_STOP, tilt_ticks)
	return
	

def write_word(loc, value):
	bus.write_word_data(addr, loc, value)
	return


def set_button_color_rgb(r, g, b):
	r = 4095 - int(round(helpers.utilities.clamp(r, 0, 4095)))
	g = 4095 - int(round(helpers.utilities.clamp(g, 0, 4095)))
	b = 4095 - int(round(helpers.utilities.clamp(b, 0, 4095)))
	bus.write_word_data(addr, LED_R_STOP, r)
	bus.write_word_data(addr, LED_G_STOP, g)
	bus.write_word_data(addr, LED_B_STOP, b)
	return


def laser_off():
	bus.write_word_data(addr, LASER_STOP, 0)
	return


def laser_on():
	bus.write_word_data(addr, LASER_STOP, 4095)
	return


def safe_state():
	bus.write_word_data(addr, PAN_START, 0)		# Move servos close to mid-point
	bus.write_word_data(addr, PAN_STOP, 1250)
	bus.write_word_data(addr, TILT_START, 0)
	bus.write_word_data(addr, TILT_STOP, 1250)
	bus.write_word_data(addr, LED_R_START, 0) 	# Turn all LEDs off
	bus.write_word_data(addr, LED_R_STOP, 4095)
	bus.write_word_data(addr, LED_G_START, 0)
	bus.write_word_data(addr, LED_G_STOP, 4095)
	bus.write_word_data(addr, LED_B_START, 0)
	bus.write_word_data(addr, LED_B_STOP, 4095)
	bus.write_word_data(addr, LASER_START, 0) 	# Turn laser off
	bus.write_word_data(addr, LASER_STOP, 0)


def shutdown():
	print 'servo_hat_shtudwon'
	safe_state()
	

def initialize():
	bus.write_byte_data(addr, 0, 0x20)			# enable the chip
	bus.write_byte_data(addr, 0xfe, 0x1e) 		# configure the chip for multi-byte write
	safe_state()
	
bus = smbus.SMBus(1) 						# the chip is on bus 1 of the available I2C buses
addr = 0x40          						# I2C address of the PWM chip.