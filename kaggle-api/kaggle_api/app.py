

import pika
import warnings

from services.callbackes import C_download_dataset

warnings.filterwarnings("ignore", category=SyntaxWarning)


def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='dataset_downloads')
    return connection, channel

def add_callbacks(channel):
    channel.basic_consume(queue='dataset_downloads', on_message_callback=C_download_dataset, auto_ack=True)

def main():
    connection, channel = setup_rabbitmq()
    add_callbacks(channel)

    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
