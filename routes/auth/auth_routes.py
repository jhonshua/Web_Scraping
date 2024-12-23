from fastapi import APIRouter, Request
from config.db_config import SessionLocal
from fastapi import Depends,Body
from controllers.auth.auth_controller import login, logout, reset
from schemas.auth.auth_schemas import   ResponseAuth, ResetPasswordRequest, InvalidTokenSchema
from schemas.user.user_schemas import Response
from sqlalchemy.orm import Session
from utils.send_mail import send_email

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# autenticar usuario
@router.post("/login")
async def user_login(body_data= Body(...),db: Session = Depends(get_db)):
        try:
                userlogin = login(body_data, db)
                if userlogin:
                        return ResponseAuth(status="Ok", 
                                code="200", 
                                message="login successfully", 
                                token = userlogin)
       
                else:
                        return ResponseAuth(status="Ok", 
                                code="401 ", 
                                message="login incorrect")
       
        except Exception as e:
                return ResponseAuth(status="Error",
                          code="500",  
                          message="User error login{e}")
        

    
# salir de seccion usuario crear una lista negra de token no validos 
@router.get("/logout/{user_id}")
async def  user_logout(request: Request, user_id: int, db: Session = Depends(get_db)):
        authorization_header = request.headers.get("Authorization")
        if authorization_header:
                data = InvalidTokenSchema(
                        token=authorization_header.split(" ")[1],
                        user_id=user_id
                        )    
                logout( data, db)
                return ResponseAuth(status="Ok", 
                          code="200", 
                          message="Session closed successfully", 
                          )
                
    
# reset pass envia un correo con la clave provisional
@router.post("/reset")
async def pass_reset(body_data= Body(...),db: Session = Depends(get_db)):
        user_data = ResetPasswordRequest(**body_data)
        try:
                data = reset(user_data, db)  
                await send_email(data)
                return Response(status="Ok", 
                        code="200", 
                        message="reset successfully").dict(exclude_none=True)
                        
        except Exception as e:
                return Response(status="Error ", code="500", message=str(e)).dict(exclude_none=True)