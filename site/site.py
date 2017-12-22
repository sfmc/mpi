from flask import Flask, render_template, request
from scheduled_lasing import ScheduledLasing

app = Flask(__name__)
#https://www.raspberrypi-spy.co.uk/2017/07/create-a-basic-python-web-server-with-flask/

@app.route("/", methods = ['POST', 'GET'])
def index():
	scheduled_lasings = []
	scheduled_lasings.append(ScheduledLasing())
	scheduled_lasings.append(ScheduledLasing())
	scheduled_lasings.append(ScheduledLasing())
	data={'scheduled_lasings':scheduled_lasings}
	if request.method == 'POST':
		return "HELLO"
	else:
		return render_template('index.html', data=data)
  
if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)