#!/bin/bash

my_apikey=$( cat mycredentials | awk '{print $3}' )
echo "hi ${my_apikey}"
curl -F apikey=${my_apikey} -F dbowner="amoghaks" -F dbname="groww_faqs_db" https://api.dbhub.io/v1/download --output ./database/groww_faqs_db

fuser -k 5055/tcp

. /home/amogh/.local/share/virtualenvs/rasaproject_2-o3mr33AT/bin/activate

sleep 1s 

rasa run actions -vv