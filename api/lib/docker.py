import os

API_URL = os.getenv("API_URL")
VOLUME_ROOT_PATH = os.getenv("SHARED_VOLUME_PATH")
RUN_TOKENIZER_CONTAINER = 'docker run -it --add-host=host.docker.internal:host-gateway -v "' + VOLUME_ROOT_PATH + ':/shared_volume" hskcoder/tokenizer:0.2 /shared_volume/input/{FILE_NAME_WITH_EXTENSION} /shared_volume/tokenizer_output ' + API_URL
RUN_WORD_COUNT_CONTAINER = 'docker run -it --add-host=host.docker.internal:host-gateway -v "' + VOLUME_ROOT_PATH + ':/shared_volume" hskcoder/word_count:0.2 /shared_volume/tokenizer_output/{FILE_NAME_WITHOUT_EXTENSION}.json /shared_volume/word_count_output ' + API_URL


def run_tokenizer_container(file_name):
    print(RUN_TOKENIZER_CONTAINER.format(
        FILE_NAME_WITH_EXTENSION = file_name
    ))
    os.popen(RUN_TOKENIZER_CONTAINER.format(
        FILE_NAME_WITH_EXTENSION = file_name
    ))



def run_word_count_container(file_name):
    os.popen(RUN_WORD_COUNT_CONTAINER.format(
        FILE_NAME_WITHOUT_EXTENSION = file_name
    ))