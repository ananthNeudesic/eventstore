#!/bin/bash
NAME_OF_EVENT="$1"
if [[ -z "$NAME_OF_EVENT" ]]; then
    echo "Enter name of event - Created/Updated"
else
    if [ -f $NAME_OF_EVENT ]; then
        curl -i -d @$NAME_OF_EVENT -H "Content-Type:application/vnd.eventstore.events+json" \
            "http://127.0.0.1:2113/streams/mystream"
        echo "Posted Event successfully"
    else
        echo "Event does not exist"
    fi
fi
## curl -i -d @event.txt -H "Content-Type:application/vnd.eventstore.events+json" \
##    "http://127.0.0.1:2113/streams/mystream"
