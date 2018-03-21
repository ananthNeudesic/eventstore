from address import Address

class Customer:

	def __init__(self):
		self.CustomerID = 0
		self.Name = ''
		self.Address = Address()

	def __init__(self, name, address):
		self.Name = name
		self.Address = address

	def __init__(self, customerid, name, address):
		self.CustomerID = customerid
		self.Name = name
		self.Address = address

	def serialize(self):
		return { 
				'customerid': str(self.CustomerID),
    			'name': str(self.Name), 
    			'address': self.Address.serialize()
    			}



