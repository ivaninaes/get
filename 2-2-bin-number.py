import RPi.GPIO as GPIO
import time
dac = [8,11,7,1,0,5,12,6]
def b(n):
    l = bin(n)[2:]
    l = '0'*(len(dac) - len(l)) + l
    d = list(l)
    for i in range(len(d)):
        d[i] = int(d[i])
    return d
nums = b(int(input()))
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, nums)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()
