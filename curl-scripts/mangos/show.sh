#!/bin/bash

curl "http://localhost:8000/screenshots/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
