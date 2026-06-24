from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.domain import ViajeCamion, ServicioCarga, Usuario
from app.schemas.domain import ViajeCamionCreate, ViajeCamionResponse, ViajeCamionUpdate, ServicioCargaCreate, ServicioCargaResponse
from app.core.security import get_current_active_user

router = APIRouter(prefix="/logistica", tags=["Logística"])

# --- Viajes Camión ---
@router.post("/viajes", response_model=ViajeCamionResponse, status_code=status.HTTP_201_CREATED)
def create_viaje(viaje: ViajeCamionCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_viaje = ViajeCamion(**viaje.model_dump())
    db.add(db_viaje)
    db.commit()
    db.refresh(db_viaje)
    return db_viaje

@router.get("/viajes", response_model=List[ViajeCamionResponse])
def get_viajes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    viajes = db.query(ViajeCamion).offset(skip).limit(limit).all()
    return viajes

@router.get("/viajes/{viaje_id}", response_model=ViajeCamionResponse)
def get_viaje(viaje_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    viaje = db.query(ViajeCamion).filter(ViajeCamion.id == viaje_id).first()
    if viaje is None:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")
    return viaje

@router.patch("/viajes/{viaje_id}", response_model=ViajeCamionResponse)
def update_viaje(viaje_id: UUID, update_data: ViajeCamionUpdate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    viaje = db.query(ViajeCamion).filter(ViajeCamion.id == viaje_id).first()
    if viaje is None:
        raise HTTPException(status_code=404, detail="Viaje no encontrado")
    
    if update_data.estado is not None:
        viaje.estado = update_data.estado
        
    db.commit()
    db.refresh(viaje)
    return viaje

# --- Servicios Carga ---
@router.post("/servicios", response_model=ServicioCargaResponse, status_code=status.HTTP_201_CREATED)
def create_servicio(servicio: ServicioCargaCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_servicio = ServicioCarga(**servicio.model_dump())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

@router.get("/servicios", response_model=List[ServicioCargaResponse])
def get_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    servicios = db.query(ServicioCarga).offset(skip).limit(limit).all()
    return servicios

@router.get("/servicios/{servicio_id}", response_model=ServicioCargaResponse)
def get_servicio(servicio_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    servicio = db.query(ServicioCarga).filter(ServicioCarga.id == servicio_id).first()
    if servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio
