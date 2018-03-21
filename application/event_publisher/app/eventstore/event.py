import uuid

class Event:

	def __init__(self):
		self.EventID = 0
		self.EventType = ''
		self.Data = ''

	def __init__(self, eventType, eventData):
		self.EventID = str(uuid.uuid4())
		self.EventType = eventType
		self.Data = eventData

	def serialize(self):
		return { 
				'eventId': self.EventID,
    			'eventType': self.EventType, 
    			'data': self.Data.serialize()
    			}
