#!/bin/bash
curl -X PUT -H "Content-Type:application/json" -d "{}" --user admin:changeit \
    "http://127.0.0.1:2113/subscriptions/mystream/mypersistentstream"
## /subscriptions/{stream}/{subscription_name}
