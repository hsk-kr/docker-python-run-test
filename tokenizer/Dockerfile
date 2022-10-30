FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install
RUN pipenv run python3 -m textblob.download_corpora

ENTRYPOINT ["pipenv", "run", "python3", "./main.py"]
