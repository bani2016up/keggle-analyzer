FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY /kaggle_api /app/kaggle_api

RUN pip install poetry

RUN poetry install

ENV KAGGLE_USERNAME=daniilparfenov
ENV KAGGLE_KEY=8ab150992b30cf3ef8b2bbe8e348c9fd
ENV logging=1

EXPOSE 9000

CMD ["poetry", "run", "python", "kaggle_api/kaggle_api.py"]
