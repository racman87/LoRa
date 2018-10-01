from pyvit import can
from pyvit.hw import cantact
import sys
import time

dev = cantact.CantactDev("/dev/tty.usbmodem1411")

dev.ser.write('S0\r'.encode())
dev.start()
count = 0
while True:
	count = count + 1
	frame = can.Frame(20)
	#frame.data = [5] * 8
	frame.data = [0xDE, 0xAD, 0xBE, 0xEF] 
	dev.send(frame)
	time.sleep(1)
	print("%d: %s" % (count, str(frame)))
