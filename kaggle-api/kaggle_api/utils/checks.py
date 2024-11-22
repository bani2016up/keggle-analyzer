import os
from typing import NoReturn

def check_kaggle_auth() -> None | NoReturn:
    if 'KAGGLE_USERNAME' not in os.environ or 'KAGGLE_KEY' not in os.environ:
        raise ValueError("Kaggle API credentials not found in environment variables. Please ensure your .env file contains KAGGLE_USERNAME and KAGGLE_KEY.")
