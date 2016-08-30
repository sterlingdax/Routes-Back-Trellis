# Use Adafruit Trellis to display routes arrival
# FIrst use buttons to light up to indicate back
# In the future, possibly interface with a PiTFT or similar

# // TODO Add a cool animation when done
# // TODO Add an animation randomly

import time
import Adafruit_Trellis
MOMENTARY = 0
LATCHING = 1
MODE = MOMENTARY

matrix0 = Adafruit_Trellis.Adafruit_Trellis()

trellis = Adafruit_Trellis.Adafruit_TrellisSet(matrix0)

NUMTRELLIS = 1

numKeys = NUMTRELLIS * 16

I2C_BUS = 1

trellis.begin((0x75, I2C_BUS))

# light up all the LEDs in order
for i in range(numKeys):
	trellis.setLED(i)
	trellis.writeDisplay()
	time.sleep(0.05)
# then turn them off
for i in range(numKeys):
	trellis.clrLED(i)
	trellis.writeDisplay()
	time.sleep(0.05)


while True:
	time.sleep(0.03)
	if MODE == MOMENTARY:
		# If a button was just pressed or released...
		if trellis.readSwitches():
			# go through every button
			for i in range(numKeys):
				# if it was pressed, turn it on
				if trellis.justPressed(i):
					print 'v{0}'.format(i)
					trellis.setLED(i)
				# if it was released, turn it off
				if trellis.justReleased(i):
					print '^{0}'.format(i)
					trellis.clrLED(i)
			# tell the trellis to set the LEDs we requested
			trellis.writeDisplay()

	if MODE == LATCHING:
		# If a button was just pressed or released...
		if trellis.readSwitches():
			# go through every button
			for i in range(numKeys):
				# if it was pressed...
				if trellis.justPressed(i):
					print 'v{0}'.format(i)
					# Alternate the LED
					if trellis.isLED(i):
						trellis.clrLED(i)
					else:
						trellis.setLED(i)
			# tell the trellis to set the LEDs we requested
			trellis.writeDisplay()

