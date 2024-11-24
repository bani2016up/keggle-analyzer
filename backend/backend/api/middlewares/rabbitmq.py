from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from utils.queue_manager import RabbitMQConnection

class RabbitMQMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        rabbitmq = RabbitMQConnection()
        rabbitmq.connect()

        request.state.rabbitmq = rabbitmq

        try:
            response = await call_next(request)
        finally:
            rabbitmq.close()
        return response
