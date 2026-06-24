import enum

class RolUsuario(str, enum.Enum):
    ADMIN = "ADMIN"
    Admin = "Admin"
    COMERCIANTE = "COMERCIANTE"
    Comerciante = "Comerciante"
    ESTIBADOR = "ESTIBADOR"
    Estibador = "Estibador"

class EstadoLicencia(str, enum.Enum):
    ACTIVA = "ACTIVA"
    SUSPENDIDA = "SUSPENDIDA"
    VENCIDA = "VENCIDA"

class EstadoEstibador(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    OCUPADO = "OCUPADO"
    INACTIVO = "INACTIVO"

class TipoCarga(str, enum.Enum):
    PERECIBLE = "PERECIBLE"
    NO_PERECIBLE = "NO_PERECIBLE"
    FRAGIL = "FRAGIL"

class EstadoViaje(str, enum.Enum):
    PROGRAMADO = "PROGRAMADO"
    EN_RUTA = "EN_RUTA"
    COMPLETADO = "COMPLETADO"
    CANCELADO = "CANCELADO"

class EstadoServicio(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    EN_PROGRESO = "EN_PROGRESO"
    FINALIZADO = "FINALIZADO"
    CANCELADO = "CANCELADO"

class EstadoSalubridadPabellon(str, enum.Enum):
    OPTIMO = "OPTIMO"
    REQUIERE_MANTENIMIENTO = "REQUIERE_MANTENIMIENTO"
    CLAUSURADO = "CLAUSURADO"

class EstadoReporte(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    EN_REVISION = "EN_REVISION"
    RESUELTO = "RESUELTO"
