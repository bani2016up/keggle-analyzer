

from typing import Literal
from pydantic import BaseModel


class ChainMetadata(BaseModel):
    exec_time: float

class ErrorModel(ChainMetadata):
    msg: str
    step: int
    analyze_type: str

class SuccessModel(ChainMetadata):
    msg: str


class ResultModel(BaseModel):
    status: Literal["success", "error", "not_executed"]
    error: ErrorModel | None
    results: list[SuccessModel]
