DEBUG = False
SAVE_DATA = False
PLOT_DATA = False

F_ref = 500
init_len = 300
buffer_len = 1000

import time
import spidev
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

F_ref = int(sys.argv[1])
print("Reference Frequency Provided = ", F_ref, "Hz")

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

while True:
	a = []
	b = []
	for x in range(init_len):
		if DEBUG:
			t1 = time.time()
			b.append(readadc(0))
			t2 = time.time()
			print((t2-t1)*1000000)
		else:
			b.append(readadc(0))
		
	# print("Acquiring Data ...")
	t1 = time.time()
	for x in range(buffer_len):
		a.append(readadc(0))
	t2 = time.time()
	Fs = buffer_len/(t2-t1)
	# print("Sampling Rate = ", Fs)

	if SAVE_DATA:
		print('Writing Data')
		with open('out.txt', 'w') as fh:
			json.dump(a, fh)

	if PLOT_DATA:
		plt.plot(a)
		plt.show()

	# Generating Reference Signals
	N = buffer_len
	t = np.linspace(0, N/Fs, N, endpoint=False)
	k = 1.0/(4*F_ref)
	s_n = np.sin(2*np.pi*F_ref*t)
	c_n = np.sin(2*np.pi*F_ref*(t + k))
	rxs = a * s_n
	rxc = a * c_n
	I_n = np.mean(rxs)      # In-phase
	Q_n = np.mean(rxc)      # Quadrature
	alpha = I_n * I_n + Q_n * Q_n

	# Final Lock-In DC Amplitude
	V = np.pi * 0.5 * np.sqrt(alpha)
	print("Lock-in R = ", int(V), "uV")