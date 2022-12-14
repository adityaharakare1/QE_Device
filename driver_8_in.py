import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode (GPIO.BCM)

f1 = 1000
f2 = 2000
f3 = 500
f4 = 700
f5 = 100
f6 = 200
f7 = 300
f8 = 400

t1 = 1/f1
t2 = 1/f2
t3 = 1/f3
t4 = 1/f4
t5 = 1/f5
t6 = 1/f6
t7 = 1/f7
t8 = 1/f8

p1state = 0
p2state = 0
p3state = 0
p4state = 0
p5state = 0
p6state = 0
p7state = 0
p8state = 0


def init_pins():
	GPIO.setup(14, GPIO.OUT)
	GPIO.output(14, 0)
	GPIO.setup(15, GPIO.OUT)
	GPIO.output(15, 0)
	GPIO.setup(20, GPIO.OUT)
	GPIO.output(20, 0)
	GPIO.setup(16, GPIO.OUT)
	GPIO.output(16, 0)
	GPIO.setup(2, GPIO.OUT)
	GPIO.output(2, 0)
	GPIO.setup(3, GPIO.OUT)
	GPIO.output(3, 0)
	GPIO.setup(4, GPIO.OUT)
	GPIO.output(4, 0)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, 0)

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
def togglep5(p5state):
	p5state = not p5state
	GPIO.output(2, p5state)
	return p5state
def togglep6(p6state):
	p6state = not p6state
	GPIO.output(3, p6state)
	return p6state
def togglep7(p7state):
	p7state = not p7state
	GPIO.output(4, p7state)
	return p7state
def togglep8(p8state):
	p8state = not p8state
	GPIO.output(17, p8state)
	return p8state

init_pins()

prevTime1 = time.time()
prevTime2 = time.time()
prevTime3 = time.time()
prevTime4 = time.time()
prevTime5 = time.time()
prevTime6 = time.time()
prevTime7 = time.time()
prevTime8 = time.time()

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
        if currTime - prevTime5 >= t5/2:
            # toggle gpio5
            p5state = togglep5(p5state)
            prevTime5 = currTime
        if currTime - prevTime6 >= t6/2:
            # toggle gpio6
            p6state = togglep6(p6state)
            prevTime6 = currTime
        if currTime - prevTime7 >= t7/2:
            # toggle gpio7
            p7state = togglep7(p7state)
            prevTime7 = currTime
        if currTime - prevTime8 >= t8/2:
            # toggle gpio8
            p8state = togglep8(p8state)
            prevTime8 = currTime

except KeyboardInterrupt:
	GPIO.cleanup()
