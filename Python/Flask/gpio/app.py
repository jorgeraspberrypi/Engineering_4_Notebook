from flask import Flask, render_template, request.1" 
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == "POST":
		print request.form
		formmsg1 = request.form.get("submitBtn1")
		formmsg2 = request.form.get("submitBtn2")
		if formmsg1 == "You clicked RED":
			if GPIO.input(17):
				GPIO.output(17,GPIO.LOW)
			else:
				GPIO.output(17,GPIO.HIGH)
		if formmsg2 == "You clicked BLUE":
			if GPIO.input(27):
				GPIO.output(27,GPIO.LOW)
			else:
				GPIO.output(27,GPIO.HIGH)
		if GPIO.input(17):
			msg1 = "Click to turn off"
		else:
			msg1 = "Click to turn on."
		if GPIO.input(27):
			msg2 = "Click to turn off."
		else:
			msg2 = "Click to turn on."
	else:
		msg1 = "No click yet."
		msg2 = "NO click yet."
	return render_template("index.html",msg1=msg1,msg2=msg2)
	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
