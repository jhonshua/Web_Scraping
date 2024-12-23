from sqlalchemy.orm import Session
from config.db_config import SessionLocal
from utils.helper_functions import verify_password, get_user_data
from models.user.user_model import User
from schemas.auth.auth_schemas import AuthSchema, InvalidTokenSchema,ResetPasswordRequest
from models.token.invalid_token import InvalidToken
from schemas.user.user_schemas import  New_userSchema
from utils.helper_functions import get_password_hash
from dotenv import load_dotenv
import random
import os
import datetime
import jwt

load_dotenv()  # Esto carga el archivo .env resolver esto segundo

CLAVE = os.getenv('CLAVE_TOKEN')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#login
def login(user_data: AuthSchema, db: Session) -> bool|str:
    
    _login = AuthSchema(**user_data) 
    user = get_user_data(db,_login.email)
    if user and verify_password(_login.password, user.password):
        # Usuario existe y contraseña válida
        expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=30)
        payload = {
            "sub": str(user.id),  # ID del usuario (puedes usar otro identificador único)
            "email":user.email,
            "exp": expiration,
        }
        secret_key = CLAVE 
        token = jwt.encode(payload, secret_key, algorithm="HS256")
        
        return token  # Usuario existe y contraseña válida.
    else:
        return False  # Usuario no existe o contraseña incorrecta
 
 
#logout
def logout(data: InvalidTokenSchema, db: Session)-> str:
    token = InvalidToken(
        user_id = data.user_id ,
        token = data.token
    ) 
    
    db.add(token)
    db.commit()
    db.refresh(token)
    token_response = ""
    return token_response

  
#reset pass
def reset(user_data: ResetPasswordRequest, db: Session) -> bool|str:
    
    email = user_data.email
    user = get_user_data(db, email)   
    if user :
        number = random.randint(100000, 999999)
        number_str = str(number)
        new_password = get_password_hash(number_str) 
        user.password = new_password 
        db.commit()
        db.refresh(user)
        data = New_userSchema(
                template="reset_email",
                name = user.full_name, 
                email = email, 
                password = number_str)
        return data
    else:
        return False  
    