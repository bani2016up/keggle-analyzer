FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
COPY .env /app/

COPY /kaggle_api /app/kaggle_api

RUN pip install poetry

RUN poetry install

COPY ./ops/start.sh /start.sh

EXPOSE 9000

ENTRYPOINT ["/bin/sh", "/start.sh"]
