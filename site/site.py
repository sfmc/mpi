from flask import Flask, render_template, request
from scheduled_lasing import ScheduledLasing

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
	scheduled_lasings = []
	scheduled_lasings.append(ScheduledLasing())
	scheduled_lasings.append(ScheduledLasing())
	scheduled_lasings.append(ScheduledLasing())
	data={'scheduled_lasings':scheduled_lasings}
	if request.method == 'POST':
		if request.form['submit'] == 'delete':
			ScheduledLasing.to_file('data.txt', scheduled_lasings)
			return "Delete: " + request.form['scheduled_lasing_to_delete']
		else:
			return "HELLO"
	else:
		return render_template('index.html', data=data)
 

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)