from picamera import PiCamera
from  time import sleep
from gpiozero import Button

button = Button(17)
camera = PiCamera()

camera.rotation = 180
camera.start_preview(fullscreen=False,window=(500,100,700,800))
frame = 1
print("ready")
while True:
	try:
		button.wait_for_press()
		print("click!")
		camera.capture('frame%03d.jpg' % frame)
		frame += 1
	except KeyboardInterrupt:
		camera.stop_preview()
		break

