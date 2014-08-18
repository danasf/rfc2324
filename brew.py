import RPi.GPIO as gpio
import time

class Brew(object):
	"""Manage a coffee pot"""
	def __init__(self, temperature=90,relay_pin=16):
		# vars we need		
		self.relay_pin = relay_pin
		self.brew_temp = temperature
		self.current_temp = 0
		self.brew_state = False

		# setup GPIO
		gpio.setmode(gpio.BCM)
		gpio.setup(self.relay_pin,gpio.OUT)
		gpio.output(self.relay_pin,False)

	def toggle_pin(self):
		self.brew_state not self.brew_state
		gpio.output(self.relay_pin,self.brew_state)

	def set_pin(self,state=True):
		self.brew_state = state
		gpio.output(self.relay_pin,self.brew_state)

	def set_temperature(self,temp):
		# check extremes
		if temp < 120 and temp > 0:
			self.brew_temp = temp
		else:
			print "Invalid temperature"

	def temp_stabilizer(self):


