#!/bin/bash

curl "http://localhost:8000/screenshots" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "screenshot": {
      "name": "'"${NAME}"'",
      "color": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo
