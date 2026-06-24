from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.domain import Pabellon, ReporteSalubridad, Usuario
from app.schemas.domain import PabellonCreate, PabellonResponse, ReporteSalubridadCreate, ReporteSalubridadResponse
from app.core.security import get_current_active_user

router = APIRouter(prefix="/salubridad", tags=["Salubridad"])

# --- Pabellones ---
@router.post("/pabellones", response_model=PabellonResponse, status_code=status.HTTP_201_CREATED)
def create_pabellon(pabellon: PabellonCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_pabellon = Pabellon(**pabellon.model_dump())
    db.add(db_pabellon)
    db.commit()
    db.refresh(db_pabellon)
    return db_pabellon

@router.get("/pabellones", response_model=List[PabellonResponse])
def get_pabellones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    pabellones = db.query(Pabellon).offset(skip).limit(limit).all()
    return pabellones

@router.get("/pabellones/{pabellon_id}", response_model=PabellonResponse)
def get_pabellon(pabellon_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    pabellon = db.query(Pabellon).filter(Pabellon.id == pabellon_id).first()
    if pabellon is None:
        raise HTTPException(status_code=404, detail="Pabellon no encontrado")
    return pabellon

# --- Reportes Salubridad ---
@router.post("/reportes", response_model=ReporteSalubridadResponse, status_code=status.HTTP_201_CREATED)
def create_reporte(reporte: ReporteSalubridadCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    db_reporte = ReporteSalubridad(**reporte.model_dump())
    db.add(db_reporte)
    db.commit()
    db.refresh(db_reporte)
    return db_reporte

@router.get("/reportes", response_model=List[ReporteSalubridadResponse])
def get_reportes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    reportes = db.query(ReporteSalubridad).offset(skip).limit(limit).all()
    return reportes

@router.get("/reportes/{reporte_id}", response_model=ReporteSalubridadResponse)
def get_reporte(reporte_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    reporte = db.query(ReporteSalubridad).filter(ReporteSalubridad.id == reporte_id).first()
    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    return reporte
