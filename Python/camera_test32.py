from picamera import PiCamera, color
from time import sleep

myCamera = PiCamera()

myCamera.start_preview(fullscreen=False,window=(300,300,400,400,))
myCamera.start_recording('myvid.h264')
sleep(10)
myCamera.stop_recording()
myCamera.stop_preview()
