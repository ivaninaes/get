import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)
def b(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]
try:
    while True:
        n = input()
        if n.isdigit():
            if int(n) >= 0 and int(n) <= 255 and float(n) % 1 == 0:
                GPIO.output(dac, b(n))
                print("{:.4f}".format(int(n)*3.3/255))
            elif int(n) < 0 or int(n) > 255:
                print('Value should be 0<=value<=255')
            elif float(n)%1 != 0:
                print('Value should be int')
        else:
            if n == 'q':
                break
            else:
                print('You should input an int number, not a string')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

