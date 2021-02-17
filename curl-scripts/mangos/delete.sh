#!/bin/bash

curl "http://localhost:8000/screenshots/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
