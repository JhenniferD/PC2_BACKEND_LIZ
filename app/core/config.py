import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "PC2 Backend"
    
    # Base de datos
    DATABASE_URL: str
    
    # Seguridad
    SECRET_KEY: str = "super-secret-key-default"
    
    # Configuración para usar un archivo .env si existe (local)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
