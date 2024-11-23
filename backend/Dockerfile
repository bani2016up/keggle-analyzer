FROM python:3.12-slim

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

COPY backend /app/backend

RUN pip install poetry

RUN poetry install

EXPOSE 9000

CMD ["poetry", "run", "python", "backend/app.py"]
