import RPi.GPIO as gpio
import time
from matplotlib import pyplot

#настраиваем gpio на Raspberry Pi

gpio.setmode(gpio.BCM)
leds = [2,3,4,17,27,22,10,9]
gpio.setup(leds, gpio.OUT)
dac = [8,11,7,1,0,5,12,6]
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
comp = 14
troyka = 13
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

#функция перевода в двоичную систему счисления

def dec2bin(n):
    return [int(i) for i in bin(int(n))[2:].zfill(8)]

#снятие показаний с troyka module

def adc():
    value = 0
    for i in range(7, -1, -1):
        value += 2**i
        gpio.output(dac, dec2bin(value))
        time.sleep(0.005)
        compValue = gpio.input(comp)
        if compValue == 1:
            value -= 2**i
    return value
try:
    results = []
    time_start = time.time()
    voltage = 0
    gpio.output(troyka, 1)

    #зарядка конденсатора, запись показаний

    print('начало зарядки конденсатора')
    while voltage < 207:
        voltage = adc()
        results.append(voltage)
        gpio.output(leds, dec2bin(voltage))
        print(voltage)
    gpio.output(troyka, 0)

    # #разрядка конденсатора, запись показаний (нерабочая на практике часть)

    # print('начало разрядки')
    # while voltage > 256*0.01:
    #     voltage = adc()
    #     results.append(voltage)
    #     gpio.output(leds, dec2bin(voltage))
    #     print(voltage)

    #фиксируем данные

    time_end = time.time()
    time_total = time_end - time_start
    period = time_total/len(results)
    freq = 1/(time_total/len(results))
    step_q = 0.01289
    #записываем данные в файлы

    print('запись данных в файл')
    with open('data.txt','w') as f:
        for i in results:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(freq) + '\n')
        f.write(str(step_q))
    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования ацп {}'.format(time_total, period, freq, step_q))

    #графики 

    print('построение графиков')
    y = [i/256*3.3 for i in results]
    x = [i*period for i in range(len(results))]
    pyplot.plot(x, y) 
    pyplot.xlabel('время')
    pyplot.ylabel('напряжение')
    pyplot.show()

finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()

