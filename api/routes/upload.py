import os
from flask import jsonify, request
from werkzeug.utils import secure_filename
from server import app
from lib import docker


@app.route("/upload", methods=["POST"])
def upload_file():
    f = request.files["file"]

    file_name = secure_filename(f.filename)
    f.save(os.path.join(os.getenv("SHARED_VOLUME_PATH"), "input", file_name))
    
    docker.run_tokenizer_container(file_name)
    
    return "succeed to upload"
    