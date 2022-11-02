import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode (GPIO.BCM)

f1 = 1000
t1 = 1/f1

pin_in = 14
pin_quad = 15

GPIO.setup(pin_in, GPIO.OUT)
GPIO.setup(pin_quad, GPIO.OUT)


try:
	while True:
		GPIO.output(pin_in, 0)
		sleep(t1/4)
		GPIO.output(pin_quad, 0)
		sleep(t1/4)
		GPIO.output(pin_in, 1)
		sleep(t1/4)
		GPIO.output(pin_quad, 1)
		sleep(t1/4)

except KeyboardInterrupt:
	GPIO.cleanup()
