import datetime, requests, json, uuid, os
from flask import Flask, request, jsonify
import feedparser as fd
from model.customer import Customer
from model.address import Address
from model.customerEvent import CustomerChanged
from eventstore.event import Event
from configuration import Configuration
from CustomJSONEncoder import CustomJSONEncoder


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
configuration = Configuration()

##Test if application is up
@app.route('/')
def index():
	return "Test page the program is running"

##Create a new Customer
@app.route('/customer', methods=['POST'])
def createCustomer():
	if not request.json:
		abort(400)
	if not 'name' in request.json or not 'address' in request.json:
		abort(400)
	address = Address(
			request.json['address']['line'],
			request.json['address']['city'],
			request.json['address']['state'],
			request.json['address']['zip']
			)
	customer = Customer(
		app.customer_id,
		request.json['name'],
		address
		)
	app.customer_id = app.customer_id + 1
	##Save the Customer
	##send CustomerCreated event
	customerEventData = CustomerChanged(
		customer
		)
	postToEventStore('CustomerCreated', customerEventData)
	##Return saved Customer
	return jsonify(customer), 201

##Update customer
@app.route('/customer/<int:customerid>', methods=['PUT'])
def updateCustomer(customerid):
	if not request.json:
		abort(400)
	if not 'name' in request.json or not 'address' in request.json:
		abort(400)
	address = Address(
			request.json['address']['line'],
			request.json['address']['city'],
			request.json['address']['state'],
			request.json['address']['zip']
			)
	customer = Customer(
		customerid,
		request.json['name'],
		address
		)
	##Update the Customer
	##send CustomerUpdated event
	customerEventData = CustomerChanged(
		customer
		)
	postToEventStore('CustomerUpdated', customerEventData)
	return jsonify(customer), 200

##Test function to read customer
@app.route('/getfeed/<int:feed_id>', methods=['GET'])
def getfeed(feed_id):
	feed = fd.parse('http://127.0.0.1:2113/streams/mystream')
	print feed['entries'][feed_id]

def postToEventStore(event, eventData):
	url = configuration.EventStoreUrl + '/streams/mystream'
	headers = {'Content-type': 'application/vnd.eventstore.events+json', 'Accept': 'application/json'}
 	event = Event(event, eventData)
  	try:
    		post_call = requests.post(url, '[' + str(event.serialize()) + ']', headers=headers)
    		print post_call.status_code, "STATUS CODE"
  	except Exception as inst:
  			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)


if __name__ == '__main__':
	app.customer_id = 0;
	print os.environ.get('EVENTSTOREPORT','2113')
	print os.environ.get('CLUSTERIP','127.0.0.1')
	app.run(host='0.0.0.0')

