import os
from utils.path import output_path
from services.schemas import DatasetDownload, StandardResponse
from services.kaggle_api import KaggleAPI


def download_dataset(dataset: DatasetDownload) -> StandardResponse:
    if os.path.exists(f"{output_path}/{dataset.name}.csv") or os.path.exists(f"{output_path}/{dataset.name}.zip"):
        return StandardResponse(status="EXISTS", msg=f"Dataset {dataset.name} already downloaded")
    KaggleAPI().download_dataset(dataset.name, output_path)
    return StandardResponse(status="DOWNLOADED", msg=f"Dataset {dataset.name} downloaded successfully")
