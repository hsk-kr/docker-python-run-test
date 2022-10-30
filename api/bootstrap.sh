#!/bin/sh

export FLASK_APP=./server.py

pipenv run flask --debug run -h 0.0.0.0 --port 20000
