# Toggle ON OFF the led
from machine import Pin, Timer
led = Pin(25, Pin.OUT)

def onoff():
    zone = int(input("0 or 1 "))

    if zone == 0:
        led.value(0)

    if zone == 1:
        led.value(1)

    else:
        print("I prefer 1.")

while True:
    onoff()
