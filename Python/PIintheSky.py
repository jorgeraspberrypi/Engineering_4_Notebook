import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303

print('Printing accelerometer & x, y, z axis values. press Ctrl-c to quit...')
while True:
accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    mystrx = 'x = ' + str(abs(accel_x/100))
    mystry = 'y = ' + str(accel_y/100)
    mystrz = 'z = ' + str(accel_z/100)
                         
