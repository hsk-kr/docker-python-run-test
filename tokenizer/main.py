import sys, json, os, requests
from textblob import TextBlob


def extract_nouns(text):
	blob = TextBlob(text)
	filtered_tags = list(filter(lambda tag: tag[1] == "NN", blob.tags))
	nouns = list(map(lambda tag: tag[0], filtered_tags))
	return nouns


def read_file(path):
	with open(path) as f:
		contents = f.read()
	return contents


def save_data(path, data):
	with open(path, "w") as f:
		json.dump(data, f)


def get_filename_from_path(path):
	return os.path.splitext(os.path.basename(path))[0]


def notify_done(url, file_name):
	requests.get(f"{url}/docker/tokenizer_done?file_name={file_name}")


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

	text = read_file(file_path)
	nouns = extract_nouns(text)

	save_data(target_path, {"nouns": nouns})
	notify_done(api_url, file_name)
 
	print("Done")