# PC2 Backend API

Backend en FastAPI listo para producción y preparado para despliegue en Railway.

## Estructura del proyecto
- `app/main.py`: Punto de entrada de la aplicación FastAPI.
- `app/database.py`: Configuración de la base de datos SQLAlchemy.
- `app/core/config.py`: Configuraciones y variables de entorno.
- `app/models/`: Modelos ORM de la base de datos.
- `app/schemas/`: Esquemas Pydantic para validación de datos.
- `app/routers/`: Rutas de la API agrupadas por recurso.
- `app/utils/`: Funciones utilitarias compartidas.

## Ejecución Local
1. Crea un entorno virtual: `python -m venv venv`
2. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Copia el archivo `.env.example` a `.env` y ajusta las variables.
5. Inicia el servidor: `uvicorn app.main:app --reload`
