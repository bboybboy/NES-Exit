""" NES-exit.py by Eric Conner on 2-6-2013
GPIO Keyboard driver for Raspberry Pi for use with external reset button on NES
"""

import uinput
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin_esc = 3

GPIO.setup(pin_esc, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if (GPIO.input(pin_esc) == 0):	# ESC button pressed
		device.emit(uinput.KEY_ESC, 1)
	else:
		device.emit(uinput.KEY_ESC, 0)

	time.sleep(.05)  # Poll every 50ms (otherwise CPU load gets too high)