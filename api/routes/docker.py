import os
from flask import jsonify, request
from server import app
from lib import docker, json


result = []


@app.route('/docker/tokenizer_done')
def get_tokenizer_done():
    file_name = request.args.get("file_name")
    docker.run_word_count_container(file_name)
    return "run a word_count container"
    

@app.route('/docker/word_count_done')
def get_word_count_done():
    file_name = request.args.get("file_name")

    json_data = json.load_data(
        os.path.join(os.getenv("SHARED_VOLUME_PATH"),
        "word_count_output",
        f"{file_name}.json"
    ))
    result.append(json_data)

    return "all works done"


@app.route('/docker/result')
def get_result():
    file_name = request.args.get("file_name")
    return jsonify({
        "result": result
    })