#importaciones
import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI as FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from config.db_config import engine
from models.rol import rol_model
from models.user import user_model
from utils.scheduler import start_scheduler

from routes.user import user_routes
from routes.rol import rol_routes

#Creamos las tablas en la base de datos (si no existen)
user_model.Base.metadata.create_all(bind=engine)
rol_model.Base.metadata.create_all(bind=engine)

# Obtener el logger específico para main.py
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Iniciando la aplicación...") # Usamos el logger correctamente
    start_scheduler()
    logger.info("API Iniciada")
    yield
    logger.info("Apagando API")

app = FastAPI(lifespan=lifespan)

# Obtener el contenido del archivo .env
load_dotenv() 

#orígenes permitidos
CORS_ORIGINS = os.getenv('CORS_ORIGINS')

#Lista de orígenes permitidos (ajústala según tus necesidades)
origins = [
   CORS_ORIGINS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener los templates genericos 
templates = Jinja2Templates(directory="templates")

#repuesta para rutas no declaradas
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse("generic_template/404.html", {"request": request})

#Incluimos las rutas relacionadas 

app.include_router(rol_routes.router, prefix="/roles", tags=["roles"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])



