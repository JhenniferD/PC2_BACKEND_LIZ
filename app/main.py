from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import traceback
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
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"detail": "Global Exception", "error": str(exc), "trace": traceback.format_exc()}
    )

from app.routers import auth, usuarios, comerciantes, estibadores, logistica, salubridad

app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(comerciantes.router)
app.include_router(estibadores.router)
app.include_router(logistica.router)
app.include_router(salubridad.router)

@app.get("/")
def read_root():
    return {"status": "API running"}
