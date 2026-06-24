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
    Activa = "Activa"
    SUSPENDIDA = "SUSPENDIDA"
    Suspendida = "Suspendida"
    VENCIDA = "VENCIDA"
    Vencida = "Vencida"

class EstadoEstibador(str, enum.Enum):
    DISPONIBLE = "DISPONIBLE"
    Disponible = "Disponible"
    OCUPADO = "OCUPADO"
    Ocupado = "Ocupado"
    INACTIVO = "INACTIVO"
    Inactivo = "Inactivo"

class TipoCarga(str, enum.Enum):
    PERECIBLE = "PERECIBLE"
    Perecible = "Perecible"
    NO_PERECIBLE = "NO_PERECIBLE"
    No_Perecible = "No_Perecible"
    No_perecible = "No_perecible"
    FRAGIL = "FRAGIL"
    Fragil = "Fragil"

class EstadoViaje(str, enum.Enum):
    PROGRAMADO = "PROGRAMADO"
    Programado = "Programado"
    EN_RUTA = "EN_RUTA"
    En_Ruta = "En_Ruta"
    En_ruta = "En_ruta"
    COMPLETADO = "COMPLETADO"
    Completado = "Completado"
    CANCELADO = "CANCELADO"
    Cancelado = "Cancelado"

class EstadoServicio(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    Pendiente = "Pendiente"
    EN_PROGRESO = "EN_PROGRESO"
    En_Progreso = "En_Progreso"
    En_progreso = "En_progreso"
    FINALIZADO = "FINALIZADO"
    Finalizado = "Finalizado"
    CANCELADO = "CANCELADO"
    Cancelado = "Cancelado"

class EstadoSalubridadPabellon(str, enum.Enum):
    OPTIMO = "OPTIMO"
    Optimo = "Optimo"
    REQUIERE_MANTENIMIENTO = "REQUIERE_MANTENIMIENTO"
    Requiere_Mantenimiento = "Requiere_Mantenimiento"
    Requiere_mantenimiento = "Requiere_mantenimiento"
    CLAUSURADO = "CLAUSURADO"
    Clausurado = "Clausurado"

class EstadoReporte(str, enum.Enum):
    PENDIENTE = "PENDIENTE"
    Pendiente = "Pendiente"
    EN_REVISION = "EN_REVISION"
    En_Revision = "En_Revision"
    En_revision = "En_revision"
    RESUELTO = "RESUELTO"
    Resuelto = "Resuelto"
