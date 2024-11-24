from fastapi import FastAPI
from api.middlewares.rabbitmq import RabbitMQMiddleware
from routes import routes

app = FastAPI()
app.add_middleware(RabbitMQMiddleware)
app.include_router(routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)
