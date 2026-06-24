from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.domain import Estibador, Usuario
from app.models.enums import EstadoEstibador
from pydantic import BaseModel
from app.schemas.domain import EstibadorCreate, EstibadorResponse
from app.core.security import get_current_active_user

router = APIRouter(prefix="/estibadores", tags=["Estibadores"])

class AsignacionRequest(BaseModel):
    placa: str

@router.post("/asignar-aleatorio", response_model=EstibadorResponse)
def asignar_aleatorio(req: AsignacionRequest, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    estibador = db.query(Estibador).filter(
        Estibador.estado.in_([EstadoEstibador.DISPONIBLE, EstadoEstibador.Disponible, EstadoEstibador.disponible]),
        Estibador.antecedentes_penales == False
    ).first()

    if not estibador:
        raise HTTPException(status_code=400, detail="No hay estibadores disponibles en este momento")

    estibador.estado = EstadoEstibador.OCUPADO
    db.commit()
    db.refresh(estibador)
    return estibador

@router.post("/", response_model=EstibadorResponse, status_code=status.HTTP_201_CREATED)
def create_estibador(estibador: EstibadorCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_estibador = Estibador(**estibador.model_dump())
    db.add(db_estibador)
    db.commit()
    db.refresh(db_estibador)
    return db_estibador

@router.get("/", response_model=List[EstibadorResponse])
def get_estibadores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    estibadores = db.query(Estibador).offset(skip).limit(limit).all()
    return estibadores

@router.get("/{estibador_id}", response_model=EstibadorResponse)
def get_estibador(estibador_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    estibador = db.query(Estibador).filter(Estibador.id == estibador_id).first()
    if estibador is None:
        raise HTTPException(status_code=404, detail="Estibador no encontrado")
    return estibador
