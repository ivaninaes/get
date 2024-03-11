# Написать Python-скрипт, который при запуске включает светодиод, если на входе 3.3В и выключает, если 0.0В:
# Не использовать цикл while
# Настроить один выбранный GPIO-пин как вход
# Настроить другой выбранный GPIO-пин как выход
# Считать значение со входа
# Подать считанное значение на выход
import RPi.GPIO as gpio  
gpio.setmode(gpio.BCM)

gpio.setup(21, gpio.OUT)
gpio.setup(19, gpio.IN)

# while True:

#     print(gpio.input(19))  

gpio.output(21, gpio.input(19))