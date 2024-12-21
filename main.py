from contextlib import asynccontextmanager
from fastapi import FastAPI
from utils.scheduler import start_scheduler
import logging  # Importamos logging en main.py

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

@app.get("/")
async def read_root():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
