import uuid
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum as SQLEnum, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.enums import RolUsuario, EstadoLicencia, EstadoEstibador, TipoCarga, EstadoViaje, EstadoServicio, EstadoSalubridadPabellon, EstadoReporte

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    rol = Column(SQLEnum(RolUsuario, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())

class Comerciante(Base):
    __tablename__ = "comerciantes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
    ruc = Column(String, unique=True, nullable=False)
    puesto = Column(String, nullable=False)
    estado_licencia = Column(SQLEnum(EstadoLicencia, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

class Estibador(Base):
    __tablename__ = "estibadores"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
    dni = Column(String, unique=True, nullable=False)
    antecedentes_penales = Column(Boolean, default=False)
    estado = Column(SQLEnum(EstadoEstibador, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

class ViajeCamion(Base):
    __tablename__ = "viajes_camion"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    placa = Column(String, nullable=False)
    origen = Column(String, nullable=False)
    tipo_carga = Column(SQLEnum(TipoCarga, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    fecha_hora_reserva = Column(DateTime(timezone=True), nullable=False)
    estado = Column(SQLEnum(EstadoViaje, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

class ServicioCarga(Base):
    __tablename__ = "servicios_carga"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    viaje_id = Column(UUID(as_uuid=True), ForeignKey("viajes_camion.id"), nullable=False)
    comerciante_id = Column(UUID(as_uuid=True), ForeignKey("comerciantes.id"), nullable=False)
    estibador_id = Column(UUID(as_uuid=True), ForeignKey("estibadores.id"), nullable=True)
    tarifa = Column(Numeric(10, 2), nullable=False)
    estado = Column(SQLEnum(EstadoServicio, values_callable=lambda obj: [e.value for e in obj]), nullable=False)

class Pabellon(Base):
    __tablename__ = "pabellones"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    estado_salubridad = Column(SQLEnum(EstadoSalubridadPabellon, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    ultima_fumigacion = Column(DateTime(timezone=True), nullable=True)

class ReporteSalubridad(Base):
    __tablename__ = "reportes_salubridad"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pabellon_id = Column(UUID(as_uuid=True), ForeignKey("pabellones.id"), nullable=False)
    descripcion = Column(String, nullable=False)
    foto_url = Column(String, nullable=True)
    estado = Column(SQLEnum(EstadoReporte, values_callable=lambda obj: [e.value for e in obj]), nullable=False)
    fecha_reporte = Column(DateTime(timezone=True), server_default=func.now())
    reportado_por = Column(UUID(as_uuid=True), ForeignKey("usuarios.id"), nullable=False)
