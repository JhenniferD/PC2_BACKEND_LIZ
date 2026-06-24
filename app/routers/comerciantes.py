from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.domain import Comerciante, Usuario
from app.schemas.domain import ComercianteCreate, ComercianteResponse
from app.core.security import get_current_active_user

router = APIRouter(prefix="/comerciantes", tags=["Comerciantes"])

@router.post("/", response_model=ComercianteResponse, status_code=status.HTTP_201_CREATED)
def create_comerciante(comerciante: ComercianteCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_comerciante = Comerciante(**comerciante.model_dump())
    db.add(db_comerciante)
    db.commit()
    db.refresh(db_comerciante)
    return db_comerciante

@router.get("/", response_model=List[ComercianteResponse])
def get_comerciantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    comerciantes = db.query(Comerciante).offset(skip).limit(limit).all()
    return comerciantes

@router.get("/{comerciante_id}", response_model=ComercianteResponse)
def get_comerciante(comerciante_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    comerciante = db.query(Comerciante).filter(Comerciante.id == comerciante_id).first()
    if comerciante is None:
        raise HTTPException(status_code=404, detail="Comerciante no encontrado")
    return comerciante
