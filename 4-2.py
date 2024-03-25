import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
try:
    while True:
        s = int(input())
        for i in range(255):
            GPIO.output(dac, dec2bin(i))
            time.sleep(int(s)/256)
        for i in range(255, -1, -1):
            GPIO.output(dac, dec2bin(i))
            time.sleep(int(s)/256)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()