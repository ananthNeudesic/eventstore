import os

class Configuration:

	def __init__(self):
		self.EventStoreIP = os.environ.get('CLUSTERIP','127.0.0.1')
		self.EventStorePort = os.environ.get('EVENTSTOREPORT','2113') 
		self.EventStoreUrl = 'http://' + str(self.EventStoreIP) + ':' + str(self.EventStorePort)
