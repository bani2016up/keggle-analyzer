FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/
COPY kaggle.json /root/.config/kaggle/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . /app
RUN chmod 600 /root/.config/kaggle/kaggle.json

EXPOSE 9000

CMD ["poetry", "run", "python", "kaggle_storage_manager/app.py"]
