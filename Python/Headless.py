
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_LSM303


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0


disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)

disp.begin()

disp.clear()
disp.display()


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
	#mystrx = 'x = ' + str(abs(accel_x/100))
	#print('Accel X {0}, Mag X={1}'.format(accel_x, mag_x))
	#time.sleep(0.5)

	#draw.text((x, top),     'Accel data', font=font, fill=255)
	#draw.text((x, top+20), mystrx, font=font, fill=255)
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	draw.rectangle((0,0,128,int(accel_x)/10), outline=0, fill=100)	


	disp.image(image)
	disp.display()


