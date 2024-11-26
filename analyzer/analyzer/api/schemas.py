from pydantic import BaseModel
from typing import List, Optional

class ChainBase(BaseModel):
    name: str
    description: Optional[str] = None

class ChainCreate(ChainBase):
    pass

class Chain(ChainBase):
    id: int
    analysis_id: int

    class Config:
        orm_mode = True

class AnalysisBase(BaseModel):
    name: str
    file_path: str

class AnalysisCreate(AnalysisBase):
    pass

class Analysis(AnalysisBase):
    id: int
    chains: List[Chain] = []

    class Config:
        orm_mode = True
