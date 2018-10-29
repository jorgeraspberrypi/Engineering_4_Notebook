#GPIO Pins Python
#Written by Kaylee and Gabby
from gpiozero import LED
from time import sleep

LED1 = LED(17)
LED2 = LED(27)

for x in range(0,10):
    LED1.on()
    LED2.on()
    sleep(0.4)
    LED1.off()
    LED2.off()
    sleep(0.4)

