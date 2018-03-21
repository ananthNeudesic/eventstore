from flask.json import JSONEncoder

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        return super(CustomJSONEncoder, self).default(obj)
