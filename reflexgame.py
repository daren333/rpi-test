from gpiozero import LED, Button
from time import time, sleep
from random import randint

led = LED(17)
button = Button(4)

while True:
    sleep(randint(1, 10))
    led.on()
    start = time()
    button.wait_for_press()
    led.off()
    end = time()
    print(end-start, 'seconds')
