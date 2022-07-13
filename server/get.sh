#!/bin/sh
curl -i -H "Content-Type: application/json;charset=utf-8 " -X GET -d '{"task_id":"'$1'"}' http://127.0.0.1:5000/image/