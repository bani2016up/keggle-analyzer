from typing import Any, Literal
from pydantic import BaseModel

class DatasetDownload(BaseModel):
    name: str


class RouteModel(BaseModel):
    method: str
    url: str
    body: Any


class CheckDataset(BaseModel):
    status: Literal["completed", "in_progress", "not_found"]
    msg: str
    name: str
