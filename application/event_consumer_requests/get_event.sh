#!/bin/bash
RUN_MODE="$1"
if [[ -z "$RUN_MODE" ]]; then
	curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/events/1
else
	curl -i -H "Content-Type: application/json" -X GET http://192.168.99.100:32001/events/1
fi
