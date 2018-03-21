#!/bin/bash
RUN_MODE="$1"
if [[ -z "$RUN_MODE" ]]; then
	curl -i -H "Content-Type: application/json" -X PUT -d @update_cust.json http://127.0.0.1:5000/customer/1
else
	curl -i -H "Content-Type: application/json" -X PUT -d @update_cust.json http://192.168.99.100:32000/customer/1
fi
