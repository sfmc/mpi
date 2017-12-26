import uuid, time, datetime
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
				scheduled_lasings.remove(to_delete)
				ScheduledLasing.to_file('data.txt', scheduled_lasings)
			return render_template('index.html', data=data)
		elif (request.form['submit'] == 'Create New'):
			return render_template('create.html', data=data)
		elif (request.form['submit'] == 'Save'):
			sl = ScheduledLasing()
			sl.DaysOfWeek['Sunday'] = True if request.form.get('sunday') else False
			sl.DaysOfWeek['Monday'] = True if request.form.get('monday') else False
			sl.DaysOfWeek['Tuesday'] = True if request.form.get('tuesday') else False
			sl.DaysOfWeek['Wednesday'] = True if request.form.get('wednesday') else False
			sl.DaysOfWeek['Thursday'] = True if request.form.get('thursday') else False
			sl.DaysOfWeek['Friday'] = True if request.form.get('friday') else False
			sl.DaysOfWeek['Saturday'] = True if request.form.get('saturday') else False
			sl.StartTime = datetime.time(14,0,0,0)
			sl.RecordVideo = True if request.form.get('record_video') else False
			sl.update()
			scheduled_lasings.append(sl)
			ScheduledLasing.to_file('data.txt', scheduled_lasings)
			return render_template('index.html', data=data)
		else:
			return render_template('index.html', data=data)
	else:
		return render_template('index.html', data=data)
 

if __name__ == "__main__":
	app.run(host='0.0.0.0',debug=True)