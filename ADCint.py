DEBUG = False

import time
import spidev
import matplotlib.pyplot as plt

print("SPI Initializing ...")
bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus,device)
spi.max_speed_hz = 4000000
spi.mode = 0

def readadc(adcnum):
	if adcnum>7 or adcnum<0:
		return -1
	r = spi.xfer2([4+(adcnum>>2),(adcnum&3)<<6,0])
	adcout = ((r[1]&15)<<8) + r[2]
	return adcout

a = []
b = []
for x in range(300):
	if DEBUG:
		t1 = time.time()
		b.append(readadc(0))
		t2 = time.time()
		print((t2-t1)*1000000)
	else:
		b.append(readadc(0))
	
print("Acquiring Data ...")
for x in range(200):
	a.append(readadc(0))

plt.plot(a)
plt.show()