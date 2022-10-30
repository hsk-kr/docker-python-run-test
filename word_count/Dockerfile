FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install pipenv
RUN pipenv install

ENTRYPOINT ["pipenv", "run", "python3", "./main.py"]
