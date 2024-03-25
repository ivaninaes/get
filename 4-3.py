import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
leds = [2,3,4,17,27,22,10,9]
GPIO.setup(leds, GPIO.OUT, initial=1)

pwm = GPIO.PWM(24, 1000)
pwm.start(0)

try:
    while True:
     dc = int(input())
     pwm.ChangeDutyCycle(dc)
     print("{:.2f}".format(dc*3.3/100))  
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()