from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Agrega estos importes para cargar desde .env
from dotenv import load_dotenv
import os

load_dotenv()  # Esto carga el archivo .env

POSTGRES_SERVER_URL = os.getenv('POSTGRES_SERVER_URL')

engine = create_engine(POSTGRES_SERVER_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()