import os
from downloader.utils.path import output_path
from downloader.services.schemas import DatasetDownload, StandardResponse
from downloader.services.kaggle_api import KaggleAPI


def download_dataset(dataset: DatasetDownload) -> str:
    path_ = f"{output_path}/{dataset.name}"
    if os.path.exists(f"{output_path}/{dataset.name}.zip"):
        return f"{path_}.zip"
    KaggleAPI().download_dataset(dataset.name, output_path)
    return f"{path_}.zip"
