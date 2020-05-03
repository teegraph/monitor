pip install -r req.txt
set FLASK_APP=monitor.py
flask db init
flask db migrate
flask db upgrade
flask run --port 8080

python sensor.py