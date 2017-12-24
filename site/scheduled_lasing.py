import time, datetime, uuid, json


def custom_converter(o):
	if isinstance(o, datetime.datetime):
		return o.__str__()
	elif isinstance(o, uuid.UUID):
		return o.__str__()
	elif isinstance(o, datetime.time):
		return o.__str__()
	else:
		raise Exception("can't serialize type " + type(o).__name__)


class ScheduledLasing():
	index = 0

	def __init__(self):
		ScheduledLasing.index += 1
		#self.id = ScheduledLasing.index
		self.id = uuid.uuid4()
		self.DaysOfWeek = ['mon']
		self.StartTime = datetime.time(14,0,0,0)
		self.DisplayedStartTime = self.StartTime.strftime("%I:%M %p")
		self.RecordVideo = False
	
	@staticmethod
	def to_file(filename, scheduled_lasings):
		json_data = [s.__dict__ for s in scheduled_lasings]
		with open(filename, 'w') as outfile:
			json.dump({'scheduled_lasings':json_data}, outfile, default = custom_converter, indent=4)
	
	@staticmethod
	def from_file(filename):
		pass