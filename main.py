from contextlib import asynccontextmanager
from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from utils.scheduler import start_scheduler
import logging  # Importamos logging en main.py
from dotenv import load_dotenv
import os

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

load_dotenv() 

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

templates = Jinja2Templates(directory="templates")

#Incluimos las rutas relacionadas 

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse("generic_template/404.html", {"request": request})


# app.include_router(user_routes.router, prefix="/users", tags=["users"])
# app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
# app.include_router(rol_routes.router, prefix="/roles", tags=["roles"])
# app.include_router(data_scraping_routes.router, prefix="/dataScraping", tags=["dataScraping"])