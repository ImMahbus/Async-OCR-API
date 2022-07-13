#!/bin/sh
curl -i -H "Content-Type: application/json" -X POST -d '@image_data/b64stringjson/'$1'' http://127.0.0.1:5000/image/