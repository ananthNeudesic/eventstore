import requests, json, os
from flask import Flask, request, jsonify
from configuration import Configuration
from CustomJSONEncoder import CustomJSONEncoder


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
configuration = Configuration()

##Test if application is up
@app.route('/')
def index():
	return "Test page the program is running. Consumer."

##Test function to read customer
@app.route('/events', methods=['GET'])
def getEvents():
	eventData = getFromEventStore(-1)
	return jsonify(eventData), 200

##Test function to read customer
@app.route('/events/<int:event_id>', methods=['GET'])
def getEventByID(event_id):
	eventData = getFromEventStore(event_id)
	return jsonify(eventData), 200

def getFromEventStore(eventID):
	url = configuration.EventStoreUrl + '/streams/mystream'
	if (eventID != -1):
		url = url + '/' + str(eventID)
	headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
  	try:
    		post_call = requests.get(url, headers=headers)
    		print post_call.status_code, "STATUS CODE"
    		return post_call.json()
  	except Exception as inst:
  			print(type(inst))    # the exception instance
			print(inst.args)     # arguments stored in .args
			print(inst)


if __name__ == '__main__':
	app.customer_id = 0;
	print os.environ.get('EVENTSTOREPORT','2113')
	print os.environ.get('CLUSTERIP','127.0.0.1')
	app.run(host='0.0.0.0')

