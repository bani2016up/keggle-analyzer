

import json
import pika
import warnings

from downloader.services.callbackes import C_download_dataset
from storage import StorageManager

warnings.filterwarnings("ignore", category=SyntaxWarning)


def setup_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='dataset_downloads')
    return connection, channel

def add_callbacks(channel):
    channel.basic_consume(queue='dataset_download', on_message_callback=C_download_dataset, auto_ack=True)
    channel.basic_consume(queue='file_operations', on_message_callback=storage_process_message, auto_ack=True)

def storage_process_message(ch, method, properties, body):
    message = json.loads(body)
    operation = message.get('operation')
    if operation == 'store':
        storage_manager.store_file(message)
    elif operation == 'read':
        storage_manager.read_file(message)
    elif operation == 'check':
        storage_manager.check_file(message)
    elif operation == 'search':
        storage_manager.search_files(message)

def main():
    connection, channel = setup_rabbitmq()
    add_callbacks(channel)
    print('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    storage_manager = StorageManager()
    main()
