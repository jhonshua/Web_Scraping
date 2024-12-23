from sqlalchemy import  Column, ForeignKey, Integer, String, BIGINT
from config.db_config import Base  # Assuming your declarative base class is here

class User(Base):
    # Name of the table in the database
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(BIGINT)  # Correcto: BIGINT en el modelo
    rol_id = Column(Integer, ForeignKey("roles.id")) 
    
