from customer import Customer
from address import Address
import datetime

class CustomerChanged:

	def __init__(self):
		self.Customer = Customer()

	def __init__(self, customer):
		self.Customer = customer
		self.UpdateTimeStamp = datetime.datetime.utcnow()

	def serialize(self):
		return { 
    			'customer': self.Customer.serialize(),
    			'updateTimeStamp': str(self.UpdateTimeStamp)
    			}



