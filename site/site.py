import uuid
from flask import Flask, render_template, request
from scheduled_lasing import ScheduledLasing

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
	scheduled_lasings = ScheduledLasing.from_file('data.txt')
	#scheduled_lasings = ScheduledLasing.dummy_data()
	#ScheduledLasing.to_file('data.txt', scheduled_lasings)
	data={'scheduled_lasings':scheduled_lasings}
	if request.method == 'POST':
		if request.form['submit'] == 'delete':
			to_delete_id = uuid.UUID(request.form['scheduled_lasing_to_delete'])
			to_delete = next((x for x in scheduled_lasings if x.id == to_delete_id), None)
			if (to_delete != None):
				print "deleting...."
				scheduled_lasings.remove(to_delete)
				ScheduledLasing.to_file('data.txt', scheduled_lasings)
			return render_template('index.html', data=data)
		else:
			return "HELLO"
	else:
		return render_template('index.html', data=data)
 

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)