from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime
from decimal import Decimal
from app.models.enums import RolUsuario, EstadoLicencia, EstadoEstibador, TipoCarga, EstadoViaje, EstadoServicio, EstadoSalubridadPabellon, EstadoReporte

# --- Usuarios ---
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    rol: RolUsuario
    activo: bool = True

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: UUID
    fecha_creacion: datetime
    
    class Config:
        from_attributes = True

# --- Comerciantes ---
class ComercianteBase(BaseModel):
    usuario_id: UUID
    ruc: str
    puesto: str
    estado_licencia: EstadoLicencia

class ComercianteCreate(ComercianteBase):
    pass

class ComercianteResponse(ComercianteBase):
    id: UUID
    
    class Config:
        from_attributes = True

# --- Estibadores ---
class EstibadorBase(BaseModel):
    usuario_id: UUID
    dni: str
    antecedentes_penales: bool = False
    estado: EstadoEstibador

class EstibadorCreate(EstibadorBase):
    pass

class EstibadorResponse(EstibadorBase):
    id: UUID
    
    class Config:
        from_attributes = True

# --- Viajes Camion ---
class ViajeCamionBase(BaseModel):
    placa: str
    origen: str
    tipo_carga: TipoCarga
    fecha_hora_reserva: datetime
    estado: EstadoViaje

class ViajeCamionCreate(ViajeCamionBase):
    pass

class ViajeCamionUpdate(BaseModel):
    estado: Optional[EstadoViaje] = None

class ViajeCamionResponse(ViajeCamionBase):
    id: UUID
    
    class Config:
        from_attributes = True

# --- Servicios Carga ---
class ServicioCargaBase(BaseModel):
    viaje_id: UUID
    comerciante_id: UUID
    estibador_id: Optional[UUID] = None
    tarifa: Decimal
    estado: EstadoServicio

class ServicioCargaCreate(ServicioCargaBase):
    pass

class ServicioCargaResponse(ServicioCargaBase):
    id: UUID
    
    class Config:
        from_attributes = True

# --- Pabellones ---
class PabellonBase(BaseModel):
    nombre: str
    categoria: str
    estado_salubridad: EstadoSalubridadPabellon
    ultima_fumigacion: Optional[datetime] = None

class PabellonCreate(PabellonBase):
    pass

class PabellonResponse(PabellonBase):
    id: UUID
    
    class Config:
        from_attributes = True

# --- Reportes Salubridad ---
class ReporteSalubridadBase(BaseModel):
    pabellon_id: UUID
    descripcion: str
    foto_url: Optional[str] = None
    estado: EstadoReporte
    reportado_por: UUID

class ReporteSalubridadCreate(ReporteSalubridadBase):
    pass

class ReporteSalubridadResponse(ReporteSalubridadBase):
    id: UUID
    fecha_reporte: datetime
    
    class Config:
        from_attributes = True
