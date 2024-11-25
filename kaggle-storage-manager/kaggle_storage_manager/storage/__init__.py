import os
import pika
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from meilisearch import Client

class StorageManager:
    def __init__(self):
        self.rabbitmq_connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        self.channel = self.rabbitmq_connection.channel()
        self.channel.queue_declare(queue='file_operations')


        meili_master_key = os.getenv('MEILISERCH_MASTER_KEY')
        if not meili_master_key:
            raise ValueError('MEILI_MASTER_KEY environment variable is not set.')

        self.meili = Client('http://meilisearch:7700', api_key=meili_master_key)
        self.meili.create_index('files')

        self.mongo = MongoClient('mongodb://mongodb:27017/')
        self.db = self.mongo['file_storage']
        self.files_collection = self.db['files']

    def store_file(self, message):
        file_path = message['file_path']
        file_name = os.path.basename(file_path)
        with open(file_path, 'rb') as file:
            content = file.read()
        file_id = self.files_collection.insert_one({
            'name': file_name,
            'content': content
        }).inserted_id
        self.meili.index('files').add_documents([{
            'id': str(file_id),
            'name': file_name
        }])
        print(f"File {file_name} stored with ID: {file_id}")

    def read_file(self, message):
        file_id = message['file_id']
        file = self.files_collection.find_one({'_id': ObjectId(file_id)})
        if file:
            print(f"File content: {file['content']}")
        else:
            print(f"File with ID {file_id} not found")

    def check_file(self, message):
        file_id = message['file_id']
        file = self.files_collection.find_one({'_id': ObjectId(file_id)})
        if file:
            print(f"File {file['name']} exists")
        else:
            print(f"File with ID {file_id} does not exist")

    def search_files(self, message):
        query = message['query']
        results = self.meili.index('files').search(query)
        for hit in results['hits']:
            print(f"Found file: {hit['name']}")
