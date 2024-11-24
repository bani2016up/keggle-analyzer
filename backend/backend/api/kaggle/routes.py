from fastapi import APIRouter, Request
from api.kaggle.schemas import DatasetDownload
import json

router = APIRouter()

@router.put("/download/")
async def download_dataset(item: DatasetDownload, request: Request) -> str:
    rabbitmq = request.state.rabbitmq

    rabbitmq.channel.basic_publish(
        exchange='',
        routing_key='dataset_downloads',
        body=json.dumps({"name": item.name})
    )

    return f"Download request for dataset {item.name} has been sent to the processing queue."


@router.put("/download/check/")
async def check_download(item: DatasetDownload, request: Request) -> str:
    rabbitmq = request.state.rabbitmq

    rabbitmq.channel.basic_publish(
        exchange='',
        routing_key='dataset_downloads',
        body=json.dumps({"name": item.name})
    )

    return f"Download request for dataset {item.name} has been sent to the processing queue."
