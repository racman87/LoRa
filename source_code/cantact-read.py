from pyvit import can
from pyvit.hw import cantact
import sys
import time

dev = cantact.CantactDev("/dev/tty.usbmodem1411")

dev.start()
count = 0
while True:
	count += 1
	print("%d: %s" % (count, str(frame)))
