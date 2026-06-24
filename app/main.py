from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database import engine, Base

# Crear las tablas en la base de datos (después se recomienda usar Alembic para migraciones)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend MVP para producción, desplegado en Railway",
    version="1.0.0"
)

# Configuración de CORS para permitir peticiones desde Vercel (frontend)
origins = [
    "http://localhost",
    "http://localhost:5173",  # Vite dev server
    "http://localhost:3000",  # Frontend dev server alternativo
    # TODO: Agregar aquí el dominio de Vercel cuando esté en producción, ej: "https://mi-app.vercel.app"
    "*"  # Permitir todos temporalmente para pruebas, cambiar en producción
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "API running"}
