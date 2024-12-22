from sqlalchemy import Column, Integer, String
from config.db_config import Base  

class InvalidToken(Base):
    __tablename__ = "invalid_tokens" 
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)  
    token = Column(String, unique=True, index=True, nullable=False)
     
