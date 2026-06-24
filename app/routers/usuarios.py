from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from app.database import get_db
from app.models.domain import Usuario
from app.schemas.domain import UsuarioCreate, UsuarioResponse
from app.utils.security import get_password_hash
from app.core.security import get_current_active_user

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    hashed_password = get_password_hash(usuario.password)
    db_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        password_hash=hashed_password,
        rol=usuario.rol,
        activo=usuario.activo
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/", response_model=List[UsuarioResponse])
def get_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    usuarios = db.query(Usuario).offset(skip).limit(limit).all()
    return usuarios

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(usuario_id: UUID, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_active_user)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario
