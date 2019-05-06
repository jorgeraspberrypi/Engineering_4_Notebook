import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

print("about to start")

while True:
	print('waiting for the  setoff')
	sensor.wait_for_setoff()
	print(GOTCHA!!!)
	GPIO.output(22, GPIO.HIGH)
	time.sleep(.2)
	GPIO.output(22, GPIO.LOW)
	sensor.wait_for_no_setoff()
	print ('clear')
	time.sleep(1)
