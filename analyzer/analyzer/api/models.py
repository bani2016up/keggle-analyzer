from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    file_path = Column(String)  # Path to the related file in kaggle-storage-manager
    chains = relationship("Chain", back_populates="analysis")

class Chain(Base):
    __tablename__ = "chains"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    analysis_id = Column(Integer, ForeignKey("analyses.id"))
    analysis = relationship("Analysis", back_populates="chains")
