import time, datetime, uuid, collections

class ScheduledLasing():
	replacements = {'Sunday':'Sun', 'Monday':'Mon', 'Tuesday':'Tue', 'Wednesday':'Wed', 'Thursday':'Thu', 'Friday':'Fri', 'Saturday':'Sat'}

	
	def getDisplayedDaysOfWeek(self):
		result = ""
		for t in self.DaysOfWeek.items():
			if (t[1] == True):
				result += ", " + self.replacements[t[0]]
		result = result[2:]
		return result
		

	def __init__(self):
		self.id = uuid.uuid4()
		self.DaysOfWeek = collections.OrderedDict()
		self.DaysOfWeek['Sunday'] = False
		self.DaysOfWeek['Monday'] = True
		self.DaysOfWeek['Tuesday'] = True
		self.DaysOfWeek['Wednesday'] = True
		self.DaysOfWeek['Thursday'] = True
		self.DaysOfWeek['Friday'] = True
		self.DaysOfWeek['Saturday'] = False
		self.StartTime = datetime.time(14,0,0,0)
		self.RecordVideo = False
		self.update()
	
	
	def update(self):
		self.DisplayedDaysOfWeek = self.getDisplayedDaysOfWeek()
		self.DisplayedStartTime = self.StartTime.strftime("%I:%M %p")
		
	
	@staticmethod
	def to_file(filename, scheduled_lasings):
		lines = ""
		for sl in scheduled_lasings:
			days_data = ",".join(['1' if a[1] else '0' for a in sl.DaysOfWeek.items()])
			row_data = days_data + "," + sl.StartTime.__str__() + "," + ('1' if sl.RecordVideo else '0')
			lines += row_data
			lines += "\n"
		with open(filename, 'w') as fp:
			fp.writelines(lines)

			
	@staticmethod
	def from_file(filename):
		result = []
		with open(filename) as f:
			lines = f.readlines()
			for line in lines:
				cols = line.strip().split(',')
				sl = ScheduledLasing()
				sl.DaysOfWeek['Sunday'] = True if (cols[0] == '1') else False
				sl.DaysOfWeek['Monday'] = True if (cols[1] == '1') else False
				sl.DaysOfWeek['Tuesday'] = True if (cols[2] == '1') else False
				sl.DaysOfWeek['Wednesday'] = True if (cols[3] == '1') else False
				sl.DaysOfWeek['Thursday'] = True if (cols[4] == '1') else False
				sl.DaysOfWeek['Friday'] = True if (cols[5] == '1') else False
				sl.DaysOfWeek['Saturday'] = True if (cols[6] == '1') else False
				sl.StartTime = cols[7]
				sl.StartTime = datetime.datetime.strptime(cols[7], '%H:%M:%S').time()
				sl.RecordVideo = True if (cols[8] == '1') else False
				sl.update()
				result.append(sl)
		return result