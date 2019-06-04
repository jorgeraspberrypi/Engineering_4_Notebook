import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_LSM303
import RPi.GPIO as GPIO
from time import sleep

lsm303 = Adafruit_LSM303.LSM303()

f = open("flightdata.py","w+")
counter = 0
# runs on crontab
# maybe a delay?
# turn on an LED or something
while counter < 40:
	time.sleep(120)
	accel, mag = lsm303.read()
	accel_x, accel_y, accel_z = accel
	mag_x, mag_y, mag_z = mag
	mystrx = 'x = ' + str(abs(accel_x/100))
	mystry = 'y = ' + str(accel_y/100)
	mystrz = 'z = ' + str(accel_z/100)
	print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
	time.sleep(0.5)
	counter += 1
	f.write(mystrx)
f.close()
