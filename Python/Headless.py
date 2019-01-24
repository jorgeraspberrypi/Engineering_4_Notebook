
import time
import Adafruit_LSM303

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

lsm303 = AdafruitLSM303.LSM303()

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()
buckets =  [0, 0]
buckets = [0] * 21
1 = 0

outline = 1
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0, width, height), outline = 0, fill =0)
padding = 2
shape_width = 50
top = padding
bottom = height-padding
x = padding
font = ImageFont.load_default()

lsm303 = Adafruit_LSM303.LSM303()

print( 'Printing accelerometer & magnetometer X axis values')
while True:
	accel, mag = lsm303.read()
	accel_x, y, z = accel
	mag_x, my, mz = mag
	accel_z = accel_z/100
	accel_y = accel_y/100
	accel_x = accel_x/100n


	draw.rectangle((0,0,width,height), outline=0, fill=0)
	if i <20:
		buckets[i]=accel_x
		for t in range(i-1)
			draw.line((t*5+10,buckets[t]*5,t*5+15,buckets[t+1]*5), fill=255)
		i = i+1
	else:
		buckets.pop(0)
		buckets.append(accel_x)
		for t in range(20):
			draw.line((t*5+10,buckets[t]*5,t*5+15,buckets[t+1]*5), fill=255)
	draw.line((10,bottom, 10, top), fill=255)
	draw.line((10,bottom, 100, bottom), fill=255)
	draw.text((85, top), 'X'+str(accel_z), font=font, fill=255)
	disp.image(image)
	disp.display()


