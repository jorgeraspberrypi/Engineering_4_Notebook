from time import sleep
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()


while True:
	filename = "intruder.h264"
	pir.wait_for_motion()
	print("Motion Detected")
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	print("Motion Gone")
	camera.stop_recording()
	sleep(0.5)


