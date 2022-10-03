import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode (GPIO.BCM)

f1 = 1000
f2 = 2000
t1 = 1/f1
t2 = 1/f2

# GPIO.setup(14, GPIO.OUT)

p1state = 0
p2state = 0


def init_pins():
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 0)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, 0)

def togglep1(p1state):
	if p1state:
		GPIO.output(14, 0)
		p1state = 0
	else:
		GPIO.output(14, 1)
		p1state = 1
	return p1state

def togglep2(p2state):
	if p2state:
		GPIO.output(15, 0)
		p2state = 0
	else:
		GPIO.output(15, 1)
		p2state = 1
	return p2state


init_pins()

prevTime1 = time.time()
prevTime2 = time.time()

try:
	while True:
		currTime = time.time()
		if currTime - prevTime1 >= t1/2:
			# toggle gpio1
			p1state = togglep1(p1state)
			prevTime1 = currTime
		if currTime - prevTime2 >= t2/2:
			# toggle gpio2
			p2state = togglep2(p2state)
			prevTime2 = currTime



except KeyboardInterrupt:
	GPIO.cleanup()

# try:
# 	while True:
# 		GPIO.output(14, 1)
# 		sleep(0.1)
# 		GPIO.output(14, 0)
# 		sleep(0.1)
# except KeyboardInterrupt:
# 	GPIO.cleanup()