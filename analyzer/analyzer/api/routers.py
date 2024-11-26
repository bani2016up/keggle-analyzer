from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas
from auth import get_current_user

router = APIRouter()

@router.post("/analyses/", response_model=schemas.Analysis)
def create_analysis(analysis: schemas.AnalysisCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_analysis = models.Analysis(**analysis.dict())
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

@router.get("/analyses/", response_model=List[schemas.Analysis])
def read_analyses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    analyses = db.query(models.Analysis).offset(skip).limit(limit).all()
    return analyses

@router.get("/analyses/{analysis_id}", response_model=schemas.Analysis)
def read_analysis(analysis_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_analysis = db.query(models.Analysis).filter(models.Analysis.id == analysis_id).first()
    if db_analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found")
    return db_analysis

@router.post("/analyses/{analysis_id}/chains/", response_model=schemas.Chain)
def create_chain_for_analysis(
    analysis_id: int, chain: schemas.ChainCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)
):
    db_analysis = db.query(models.Analysis).filter(models.Analysis.id == analysis_id).first()
    if db_analysis is None:
        raise HTTPException(status_code=404, detail="Analysis not found")
    db_chain = models.Chain(**chain.dict(), analysis_id=analysis_id)
    db.add(db_chain)
    db.commit()
    db.refresh(db_chain)
    return db_chain

@router.get("/chains/", response_model=List[schemas.Chain])
def read_chains(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    chains = db.query(models.Chain).offset(skip).limit(limit).all()
    return chains

@router.get("/chains/{chain_id}", response_model=schemas.Chain)
def read_chain(chain_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_chain = db.query(models.Chain).filter(models.Chain.id == chain_id).first()
    if db_chain is None:
        raise HTTPException(status_code=404, detail="Chain not found")
    return db_chain

@router.put("/chains/{chain_id}", response_model=schemas.Chain)
def update_chain(chain_id: int, chain: schemas.ChainCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_chain = db.query(models.Chain).filter(models.Chain.id == chain_id).first()
    if db_chain is None:
        raise HTTPException(status_code=404, detail="Chain not found")
    for key, value in chain.dict().items():
        setattr(db_chain, key, value)
    db.commit()
    db.refresh(db_chain)
    return db_chain

@router.delete("/chains/{chain_id}", response_model=schemas.Chain)
def delete_chain(chain_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_chain = db.query(models.Chain).filter(models.Chain.id == chain_id).first()
    if db_chain is None:
        raise HTTPException(status_code=404, detail="Chain not found")
    db.delete(db_chain)
    db.commit()
    return db_chain
