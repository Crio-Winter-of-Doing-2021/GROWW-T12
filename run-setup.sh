#!/bin/bash

. /home/amogh/.local/share/virtualenvs/GROWW-T12-vuEtGIJx/bin/activate

fuser -k 7000/tcp
fuser -k 8000/tcp
fuser -k 5005/tcp
fuser -k 5055/tcp
fuser -k 3000/tcp
cd backend
python3 manage.py runserver 7000 &

cd ../frontend
npm start &

cd ..

cd groww_bot
rasa run actions -vv &
docker run -p 8000:8000 rasa/duckling &

rasa run -m models --enable-api --cors "*" --debug

