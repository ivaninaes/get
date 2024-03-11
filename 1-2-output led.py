import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.OUT)

for i in range(10):
    gpio.output(21, 1)
    time.sleep(1)
    gpio.output(21,0)
    time.sleep(1)
