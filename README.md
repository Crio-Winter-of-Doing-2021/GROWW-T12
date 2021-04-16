# GROWW-T12

Team ID: GROWW-T12 | Team Members: Amogha KS &amp; Vinod Kumar Wagh

## PROJECT

Contextual Chat Bot for Investors

Installation commands

    python3 -m venv ./venv
    - then activate virtual environment

    pip3 install -U pip
    pip3 install rasa
    pip install pandas

    pip install python-socketio==4.6.1
    pip install python-engineio==3.13.2

RASA shell commands

    rasa shell // --debug ; to run in debug mode
    rasa run actions -vv // when you have custom actions defined, you need to run this before testing the bot
    rasa run -m models --enable-api --cors "*" --debug
    rasa run -m models --enable-api --cors "*" -p <port_number>
    rasa interactive // to test and modify bot responses
