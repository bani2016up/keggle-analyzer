import os
import json

from dotenv import load_dotenv


def main():
    # generates kaggle json file from env to build docker compose
    # the file is located during the build at kaggle-api/
    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")

    kaggle_json = {
        "username": username,
        "key": key
    }

    with open("kaggle-storage-manager/kaggle.json", "w") as f:
        json.dump(kaggle_json, f)



if __name__ == "__main__":
    load_dotenv()
    main()
