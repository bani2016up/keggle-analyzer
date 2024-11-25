from pydantic import BaseModel


class DatasetDownload(BaseModel):
    name: str

class StandardResponse(BaseModel):
    status: str
    msg: str
