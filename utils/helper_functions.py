from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models.user.user_model import User



#login-----------------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_user_data(db: Session, user_email: str):
    user = db.query(User).filter(User.email == user_email).first()
    return user 


