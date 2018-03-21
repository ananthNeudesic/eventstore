from flask.json import JSONEncoder
from model.customer import Customer
from model.address import Address
from eventstore.event import Event

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Customer):
            return obj.serialize()
        if isinstance(obj, Event):
        	return obj.serialize()
        return super(MyJSONEncoder, self).default(obj)
