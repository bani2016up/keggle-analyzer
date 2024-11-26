from fastapi import APIRouter, Depends, HTTPException, Request
from api.kaggle.schemas import DatasetDownload, RouteModel, CheckDataset
from backend.utils.auth import get_current_user
from utils.queue_manager import DownloadRpcClient
import json

router = APIRouter()

@router.put("/download/")
async def download_dataset(item: DatasetDownload, request: Request, user: dict = Depends(get_current_user)) -> str:
    status = (await check_download(item, request))
    if status in ["completed", "in_progress"]:
        return f"Dataset {item.name} exists. Download status: {status}."

    rabbitmq = request.state.rabbitmq

    rabbitmq.channel.basic_publish(
        exchange='',
        routing_key='dataset_downloads',
        body=RouteModel(body={"name": item.name}, method='put', url='/upload').model_dump_json()
    )

    return f"Download request for dataset {item.name} has been sent to the processing queue."


@router.get("/download/check/")
async def check_download(item: DatasetDownload, request: Request, user: dict = Depends(get_current_user)) -> CheckDataset:
    rabbitmq = request.state.rabbitmq

    rpc_client = DownloadRpcClient(rabbitmq)
    message = RouteModel(body={"name": item.name}, method='GET', url='/check').model_dump_json()

    try:
        response = rpc_client.call(message)
        response_data = json.loads(response)

        if response_data.get('status') == 'completed':
            return CheckDataset(status="completed", msg=f"Download of dataset {item.name} has been completed.", name=item.name)
        elif response_data.get('status') == 'in_progress':
            return CheckDataset(status="in_progress", msg=f"Download of dataset {item.name} is still in progress.", name=item.name)
        elif response_data.get('status') == 'not_found':
            return CheckDataset(status="not_found", msg=f"Dataset {item.name} was not found in the download queue.", name=item.name)
        else:
            return CheckDataset(status="unknown", msg=f"Unknown status for dataset {item.name}.", name=item.name)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error checking download status: {str(e)}"
        ) from e
