import time, datetime, uuid, collections

class ScheduledLasing():
	index = 0
	replacements = {'Sunday':'Sun', 'Monday':'Mon', 'Tuesday':'Tue', 'Wednesday':'Wed', 'Thursday':'Thu', 'Friday':'Fri', 'Saturday':'Sat'}
	
	def getDisplayedDaysOfWeek(self):
		result = ""
		for t in self.DaysOfWeek.items():
			if (t[1] == True):
				result += ", " + self.replacements[t[0]]
		result = result[2:]
		return result
		

	def __init__(self):
		ScheduledLasing.index += 1
		#self.id = ScheduledLasing.index
		self.id = uuid.uuid4()
		self.DaysOfWeek = collections.OrderedDict()
		self.DaysOfWeek['Sunday'] = False
		self.DaysOfWeek['Monday'] = True
		self.DaysOfWeek['Tuesday'] = True
		self.DaysOfWeek['Wednesday'] = True
		self.DaysOfWeek['Thursday'] = True
		self.DaysOfWeek['Friday'] = True
		self.DaysOfWeek['Saturday'] = False
		self.DisplayedDaysOfWeek = self.getDisplayedDaysOfWeek()
		self.StartTime = datetime.time(14,0,0,0)
		self.DisplayedStartTime = self.StartTime.strftime("%I:%M %p")
		self.RecordVideo = False
	
	@staticmethod
	def to_file(filename, scheduled_lasings):
		lines = ""
		for sl in scheduled_lasings:
			days_data = ",".join(['1' if a[1] else '0' for a in sl.DaysOfWeek.items()])
			lines += days_data
			lines += "\n"
		with open(filename, 'w') as fp:
			fp.writelines(lines)
	
	@staticmethod
	def from_file(filename):
		
		
		pass