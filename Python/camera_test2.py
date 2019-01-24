from picamera import PiCamera
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(300,300,400,400))
sleep(5)

for effect in myCamera.IMAGE_EFFECTS:
	myCamera.image_effect = effect
	print(effect)
	if effect == "film" or effect == "sketch" or effect == "blur" or effect == "emboss" or effect == "cartoon":
		name =  'ima%s.jpg'% effect
		print(name)
		myCamera.capture(name)
	sleep(2)
myCamera.stop_preview()

