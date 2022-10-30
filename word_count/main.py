import sys, json, os, requests


def count_word(nouns_list):
	count_dict = dict()

	for noun in nouns_list:
		if noun in count_dict:
			count_dict[noun] += 1
		else:
			count_dict[noun] = 1

	return count_dict


def load_data(path):
	with open(path) as f:
		json_data = json.load(f)
	return json_data


def save_data(path, data):
	with open(path, "w") as f:
		json.dump(data, f)


def get_filename_from_path(path):
	return os.path.splitext(os.path.basename(path))[0]


def notify_done(url, file_name):
	requests.get(f"{url}/docker/word_count_done?file_name={file_name}")


if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("You must pass file path as an argument")
		print("python3 main.py [file path to read] [dir to save] [notification api]")
		print("Example) python3 main.py ./test.txt ./ http://host.docker.internal:20000")
		sys.exit()
	
	api_url = sys.argv[3]
	file_path = sys.argv[1]
	file_name = get_filename_from_path(file_path)
	target_path = os.path.join(sys.argv[2], file_name + ".json") 

	json_data = load_data(file_path)
	count_dict = count_word(json_data["nouns"])

	save_data(target_path, {"result": count_dict})
	notify_done(api_url, file_name)
	print("Done")
