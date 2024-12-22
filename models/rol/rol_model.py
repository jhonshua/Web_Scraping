from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from config.db_config import Base  # Assuming your declarative base class is here
from sqlalchemy_utils import JSONType 

class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    ability = Column(JSONType) 
 