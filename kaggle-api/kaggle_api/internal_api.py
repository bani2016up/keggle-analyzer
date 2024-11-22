from utils.checks import check_kaggle_auth
from utils.startup import load_dotenv

load_dotenv()
check_kaggle_auth()


from fastapi import FastAPI
from pydantic import BaseModel
from kaggle_api import KaggleAPI
from utils.path import output_path
import os



app = FastAPI()


class DatasetDownload(BaseModel):
    name: str

class StandardResponse(BaseModel):
    status: str
    msg: str

@app.put("/download/")
async def update_item(dataset: DatasetDownload) -> StandardResponse:
    print(f"{output_path}/{dataset.name}.csv")
    if os.path.exists(f"{output_path}/{dataset.name}.csv") or os.path.exists(f"{output_path}/{dataset.name}.zip"):
        return StandardResponse(status="EXISTS", msg=f"Dataset {dataset.name} already downloaded")
    KaggleAPI().download_dataset(dataset.name, output_path)
    return StandardResponse(status="DOWNLOADED", msg=f"Dataset {dataset.name} downloaded successfully")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
