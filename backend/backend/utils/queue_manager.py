import uuid
import pika
from pika.adapters.blocking_connection import BlockingChannel

class RabbitMQConnection:
    def __init__(self):
        self.connection = None
        self.channel: BlockingChannel = None

    def connect(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
        self.channel: BlockingChannel = self.connection.channel()
        self.channel.queue_declare(queue='dataset_download')

    def close(self):
        if self.connection:
            self.connection.close()

class DownloadRpcClient:
    def __init__(self, rabbitmq: RabbitMQConnection):
        self.connection = rabbitmq.connection
        self.channel = rabbitmq.channel
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, body):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='dataset_downloads',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=body)
        while self.response is None:
            self.connection.process_data_events()
        return self.response
