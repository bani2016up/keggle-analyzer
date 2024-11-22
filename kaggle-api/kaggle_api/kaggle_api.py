import os
from typing import Optional
from kaggle.api.kaggle_api_extended import KaggleApi


class KaggleAPI:

    def __init__(self, env_file: Optional[str] = None) -> None:
        self.api = KaggleApi()
        self.api.authenticate()

    def download_dataset(self, dataset_name: str, path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)

        self.api.dataset_download_files(dataset_name, path=path)

    def list_datasets(self):
        return self.api.dataset_list()
