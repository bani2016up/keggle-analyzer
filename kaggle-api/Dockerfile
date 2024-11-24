FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY /kaggle_api /app/kaggle_api
COPY kaggle.json /root/.config/kaggle/

RUN pip install poetry

RUN poetry install
RUN chmod 600 /root/.config/kaggle/kaggle.json

EXPOSE 9000

CMD ["poetry", "run", "python", "kaggle_api/app.py"]
