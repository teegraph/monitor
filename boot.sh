#!/bin/bash
source venv/bin/activate
flask db init
flask db migrate
flask db upgrade
flask run --port 8080