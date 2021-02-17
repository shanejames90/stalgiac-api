#!/bin/bash

curl "http://localhost:8000/screenshots" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
