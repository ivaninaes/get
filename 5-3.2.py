import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
leds = [2,3,4,17,27,22,10,9]
comp = 14
troyka = 13
levels = 2**8
maxVoltage = 3.3
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=1)

def b(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]

def adc():
    value = 0
    sign = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(7, -1, -1):
        value += 2**i
        time.sleep(0.0007)
        sign = b(value)
        GPIO.output(dac, sign)
        compValue = GPIO.input(comp)
        if compValue == 1:
            value -= 2**i
        return value

try:
    while True:
        n = adc()
        GPIO.output(leds, b(n))
        time.sleep(0.05)
finally:
    print('adasd')
    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()
