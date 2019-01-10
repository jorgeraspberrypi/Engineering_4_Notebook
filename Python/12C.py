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

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
padding = 2
shape_width = 20
top = padding
bottom = height-padding
draw = ImageDraw.Draw(image)
x = padding
font = ImageFont.load_default()

lsm303 = Adafruit_LSM303.LSM303()

print('Printing accelerometer & x, y, z axis values. press Ctrl-c to quit...')
while True:
    draw.rectangle((0,0, width,height), outline=0, fill=0)
    accel, mag = lsm303.read()
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    mystrx = 'x = ' + str(abs(accel_x/100))
    mystry = 'y = ' + str(accel_y/100)
    mystrz = 'z = ' + str(accel_z/100)
                         
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    time.sleep(0.5)

    draw.text((x, top),    'Accel data',  font=font, fill=255)
    draw.text((x, top+20), mystrx, font=font, fill=255)
    draw.text((x, top+30), mystry, font=font, fill=255)
    draw.text((x, top+40), mystrz, font=font, fill=255)

    disp.image(image)
    disp.display()
