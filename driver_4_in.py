import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode (GPIO.BCM)

f1 = 1300
f2 = 550
f3 = 1300
f4 = 550

t1 = 1/f1
t2 = 1/f2
t3 = 1/f3
t4 = 1/f4

p1state = 0
p2state = 0
p3state = 0
p4state = 0


def init_pins():
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 0)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, 0)
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, 0)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, 0)

def togglep1(p1state):
	p1state = not p1state
	GPIO.output(14, p1state)
	return p1state
def togglep2(p2state):
	p2state = not p2state
	GPIO.output(15, p2state)
	return p2state
def togglep3(p3state):
	p3state = not p3state
	GPIO.output(20, p3state)
	return p3state
def togglep4(p4state):
	p4state = not p4state
	GPIO.output(16, p4state)
	return p4state

init_pins()

prevTime1 = time.time()
prevTime2 = time.time()
prevTime3 = time.time()
prevTime4 = time.time()

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
		if currTime - prevTime3 >= t3/2:
			# toggle gpio3
			p3state = togglep3(p3state)
			prevTime3 = currTime
		if currTime - prevTime4 >= t4/2:
			# toggle gpio4
			p4state = togglep4(p4state)
			prevTime4 = currTime




except KeyboardInterrupt:
	GPIO.cleanup()
