DEBUG = False
SAVE_DATA = False
PLOT_DATA = False

F_ref_1 = 500
F_ref_2 = 1000
init_len = 300
buffer_len = 1000
avg_len = 10

import time
import spidev
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

F_ref_1 = int(sys.argv[1])
F_ref_2 = int(sys.argv[2])
print("Reference Frequencies Provided = ", F_ref_1," ", F_ref_2, "Hz")

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
	sum1 = 0
	sum2 = 0
	for i in range(0, avg_len):
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
		k1 = 1.0/(4*F_ref_1)
		s_n_1 = np.sin(2*np.pi*F_ref_1*t)
		c_n_1 = np.sin(2*np.pi*F_ref_1*(t + k))
		rxs_1 = a * s_n_1
		rxc_1 = a * c_n_1
		I_n_1 = np.mean(rxs_1)      # In-phase
		Q_n_1 = np.mean(rxc_1)      # Quadrature
		alpha_1 = I_n_1 * I_n_1 + Q_n_1 * Q_n_1
			
		k2 = 1.0/(4*F_ref_2)
		s_n_2 = np.sin(2*np.pi*F_ref_2*t)
		c_n_2 = np.sin(2*np.pi*F_ref_2*(t + k))
		rxs_2 = a * s_n_2
		rxc_2 = a * c_n_2
		I_n_2 = np.mean(rxs_2)      # In-phase
		Q_n_2 = np.mean(rxc_2)      # Quadrature
		alpha_2 = I_n_2 * I_n_2 + Q_n_2 * Q_n_2

		# Final Lock-In DC Amplitude
		V_1 = np.pi * 0.5 * np.sqrt(alpha_1)
		V_2 = np.pi * 0.5 * np.sqrt(alpha_2)
		sum1 = sum1 + V_1
		sum2 = sum2 + V_2
	
	print("Lock-in R = (", F_ref_1, ") ", int(sum1/avg_len)," (", F_ref_2, ") ",int(sum2/avg_len), "uV")