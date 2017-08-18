#!/bin/bash

echo "hello"

curl -u admin:admin -X POST -H 'Content-Type: application/json' -d'{"type":"page","title":"new page", "space":{"key":"AP"},"body":{"storage":{"value":"<p>This is a new page</p>","representation": "storage"}}}' http://192.168.100.76:8090/confluence/rest/api/content/ | python3 -mjson.tool
