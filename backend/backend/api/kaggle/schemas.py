from pydantic import BaseModel

class DatasetDownload(BaseModel):
    name: str
