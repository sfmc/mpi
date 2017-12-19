#!/usr/bin/python
import math

def clamp(v, min_value, max_value):
	return max(min_value, min(max_value, v))


def drange(start, stop, step):
     r = start
     while r < stop:
         yield r
         r += step