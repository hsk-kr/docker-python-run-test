$env:FLASK_APP = './server.py'

python3 -m pipenv run flask --debug run -h 0.0.0.0 --port 20000