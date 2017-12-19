#!/usr/bin/python
import math, collections, time
import interfaces.servo_hat
import helpers.utilities

Color = collections.namedtuple("Color", ["r", "g", "b"])
WHITE = Color(120, 220, 255)
BLACK = Color(0, 0, 0)
RED = Color(105, 0, 0)
ORANGE = Color(90, 100, 0)
YELLOW = Color(80, 160, 0)
GREEN = Color(0, 120, 0)
CYAN = Color(0,120,200)
BLUE = Color(4, 4, 255)
PURPLE = Color(80, 0, 210)
ALL_COLORS = [WHITE, RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE]


def scale_color(color, multiplier):
	multiplier = multiplier**4 # gamma correction
	r = color.r * multiplier
	g = color.g * multiplier
	b = color.b * multiplier
	return Color(r,g,b)


def set_button_color(rgb_color, intensity = 1.0):
	if (intensity != 1):
		rgb_color = scale_color(rgb_color, intensity)
	interfaces.servo_hat.set_button_color_rgb(16*rgb_color.r, 16*rgb_color.g, 16*rgb_color.b)
	return

	
def glow(color, duration):
	time_step = 0.05
	half_duration = duration / 2.0
	set_button_color(BLACK)
	for i in helpers.utilities.drange (0, half_duration, time_step):
		time.sleep(time_step)
		set_button_color(color, i / half_duration)
	for i in helpers.utilities.drange (0, half_duration, time_step):
		time.sleep(time_step)
		set_button_color(color, (half_duration - i) / half_duration)
	set_button_color(BLACK)


def glow_all_colors():
	for color in ALL_COLORS:
		glow(color, 1)
	set_button_color(BLACK)	