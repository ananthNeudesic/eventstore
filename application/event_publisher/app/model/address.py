class Address:

	def __init__(self):
		self.Line = ''
		self.City = ''
		self.State = ''
		self.Zip = ''

	def __init__(self, line, city, state, zipcode):
		self.Line = line
		self.City = city
		self.State = state
		self.Zip = zipcode

	def serialize(self):
		return { 
    			'line': str(self.Line), 
    			'city': str(self.City),
    			'state': str(self.State),
    			'zip': str(self.Zip)
    			}
