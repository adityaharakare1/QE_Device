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
p1qstate = 0
p2qstate = 0


def init_pins():
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 0)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, 0)
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, 0)
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, 0)

def togglep1(p1state):
	if p1state:
		GPIO.output(14, 0)
		p1state = 0
	else:
		GPIO.output(14, 1)
		p1state = 1
	return p1state
def togglep1q(p1qstate):
	if p1qstate:
		GPIO.output(20, 0)
		p1qstate = 0
	else:
		GPIO.output(20, 1)
		p1qstate = 1
	return p1qstate

def togglep2(p2state):
	if p2state:
		GPIO.output(15, 0)
		p2state = 0
	else:
		GPIO.output(15, 1)
		p2state = 1
	return p2state
def togglep2q(p2qstate):
	if p2qstate:
		GPIO.output(21, 0)
		p2qstate = 0
	else:
		GPIO.output(21, 1)
		p2qstate = 1
	return p2qstate


init_pins()

prevTime1 = time.time()
prevTime2 = time.time()

prevTime1q = prevTime1 + t1/4
prevTime2q = prevTime2 + t2/4


try:
	while True:
		currTime = time.time()
		print((prevTime1q-prevTime1)*1000)
		if currTime - prevTime1 >= t1/2:
			# toggle gpio1
			p1state = togglep1(p1state)
			prevTime1 = currTime

		if currTime - prevTime1q >= t1/2:
			# toggle gpio1q
			p1qstate = togglep1q(p1qstate)
			prevTime1q = currTime

		if currTime - prevTime2 >= t2/2:
			# toggle gpio2
			p2state = togglep2(p2state)
			prevTime2 = currTime

		
		if currTime - prevTime2q >= t2/2:
			# toggle gpio2q
			p2qstate = togglep2q(p2qstate)
			prevTime2q = currTime




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