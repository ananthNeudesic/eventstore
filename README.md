# Event Store - How to quick guide

This guide illustrates the use of Event Store

* Installation and running in Docker
* Creating and using streams
* Creating Projections

## Getting Started

### Prerequisites

Docker toolset needs to be installed
Python is installed

### Installation - Event Store

Download the docker hub image for Event Store

```
docker pull eventstore/eventstore
```

Run the Event Store image in local machine

```
docker run --name myeventstore -it \
  -p 2113:2113 -p 1113:1113 eventstore/eventstore
```

* -it - Run the eventstore in interactive mode
* -p 2113:2113 - Match the nodes port to Host port to make Admin UI work
* -p 1113:1113 - NEED TO FIND OUT WHY

### Installation - Python

Install virtualenv for Python from https://pypi.python.org/pypi/virtualenv
Note: This creates a private python environment in 'eventstoreapp'

```
python ./virtualenv-15.1.0/virtualenv.py ./eventstoreapp
```

Install Python feedparser by downloading the zip from https://github.com/kurtmckee/feedparser and unzipping to a folder under 'eventstoreapp'


```
sudo -H ./../bin/pip install feedparser
```

Install Flask for python application

```
sudo ../../bin/pip install flask
```

## Interactive mode

Logging on into Event store interactively

http://127.0.0.1:2113/

* default user id : admin
* default password : changeit

## Publisher

### Create and post to a stream

Simulate event data generated from a program. 

```
[
  {
    "eventId": "d3910e5f-0eff-408a-988a-b9e1c5ed86bc",
    "eventType": "CustomerCreated",
    "data": { 
      "id": "1001", 
      "name": "Name of Customer", 
      "phone": "2223334444",
      "address" : {
        "line1" : "1 N Main Street",
        "city" : "Santa Ana",
        "state" : "CA",
        "zip" : "91355"
      }
    }
  }
]
```
* eventId - unique event guid for every event
* data - Event data in Json format.

Post data to 'mystream'

```
curl -i -d @CustCreatedEvent.txt \
    -H "Content-Type:application/vnd.eventstore.events+json" \
    "http://127.0.0.1:2113/streams/mystream"
```


### Test the stream

Viewing the stream information

```
curl -i -H "Accept:application/vnd.eventstore.atom+json" \
    "http://127.0.0.1:2113/streams/mystream"
```

Viewing a message in a stream

```
curl -i -H "Accept:application/vnd.eventstore.atom+json" \
    "http://127.0.0.1:2113/streams/mystream/0"
```


## Subscriber

### Volatile Subscriber

* Subscribe to events only when subscription is active (between start and stop)
* Run this program from locally installed python

```
import feedparser as fd
feed=fd.parse('http://127.0.0.1:2113/streams/mystream')
print feed['entries'][0]
```
This will read all the entries for a stream

### Catch-Up Subscriber

* Subscribe to events from a certain start point
** event number
** transaction file position

HOW TO CREATE

### Persistent Subscriber

* Subscription state stored on server
* Guarantees atleast-once-delivery to subscriber

```
curl -X PUT -H "Content-Type:application/json" \
    -d "{}" --user admin:changeit \
    "http://127.0.0.1:2113/subscriptions/mystream/mypersistentstream"

```

## Projections

### Create projection - All Events

* Name - CountAllCustomerEvent
* Mode - Continuous
```
fromStream("mystream")
  .when(
      {
         $all : function(state, event) {
             return state + 1;
         }
      }
  );
```

### Create projection - Created Event

* Name - CountCustomerCreatedEvent
* Mode - Continuous
```
fromStream("mystream")
  .when({
       "CustomerCreated" : function (state, event) {
           return state + 1;
       }  
    }
  );
```

### Create projection - Updated Events

* Name - CountCustomerUpdatedEvent
* Mode - Continuous
```
fromStream("mystream")
  .when({
       "CustomerUpdated" : function(state, event) {
           return state + 1;
       }  
    }
  );
```
## Deployment

### Create a Pod for running EventStore docker

```
apiVersion: v1
kind: Pod
metadata:
  name: myeventstore
  labels:
    app: eventstore
spec:
  containers :
    - image: eventstore/eventstore
      name: myeventstore
      ports:
        - containerPort: 1113
        - containerPort: 2113
```

### Create a service

* Note to map port 1113 and 2113 to port between 30000 and 32767

```
apiVersion: v1
kind: Service
metadata:
  name: myeventstoresvc
spec:
  selector:
    app: eventstore
  type: NodePort
  ports:
    - name: tcp1
      port: 1113
      targetPort: 1113
      nodePort: 31113
      protocol: TCP
    - name: tcp2
      port: 2113
      targetPort: 2113
      nodePort: 32113
      protocol: TCP
```
## Clean Up

Stopping and deleting the container

```
docker container stop myeventstore
docker container rm myeventstore
```

## Authors

Ananth Raghavendra

## License

## Acknowledgements

* https://eventstore.org
* https://github.com/EventStore/EventStore/wiki
