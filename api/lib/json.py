import json


def load_data(path):
	with open(path) as f:
		json_data = json.load(f)
	return json_data