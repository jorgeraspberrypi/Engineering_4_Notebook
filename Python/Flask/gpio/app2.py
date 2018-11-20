from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
tput(17,GPIO.HIGH)
                 #               GPIO.output(27,GPIO.HIGH)
                  #              msg1 == "CLick to turn off."
                   #             msg2 = "something"
		msg1 = "post"
		msg2 = "post"
	else:
		msg1 = "No click yet."
		msg2 = "NO click yet."
	#return render_template("index.html",msg1=msg1,msg2=msg2)
	return("hi")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
