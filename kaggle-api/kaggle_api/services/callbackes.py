
import json
from services.schemas import DatasetDownload
from services import download_dataset


def C_download_dataset(ch, method, properties, body):
    data = json.loads(body)
    dataset = DatasetDownload(name=data['name'])
    result = download_dataset(dataset)
    print(f"Processed: {result}")
