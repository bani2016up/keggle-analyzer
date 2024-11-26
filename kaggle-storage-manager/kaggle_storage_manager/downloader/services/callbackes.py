import json
import pika
from downloader.services.schemas import DatasetDownload
from downloader.services import download_dataset

def C_download_dataset(ch, method, properties, body):
    data = json.loads(body)
    dataset = DatasetDownload(name=data['name'])
    path_to_dataset = download_dataset(dataset)

    # Send the dataset to storage service
    send_to_storage(ch, path_to_dataset)

def send_to_storage(channel, file_path):

    message = {
        'operation': 'store',
        'file_path': file_path
    }

    # Publish the message
    channel.basic_publish(exchange='',
                          routing_key='file_operations',
                          body=json.dumps(message))

    print(f" [x] Sent 'store' request for {file_path}")
