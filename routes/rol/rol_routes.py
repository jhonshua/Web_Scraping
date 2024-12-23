from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status,Body
from schemas.roles.roles_schemas import   Response ,RolSchema
from controllers.roles.roles_controller import get_all_rol, create_rol, delete_rol, get_rol, update_rol
from config.db_config import SessionLocal
from middleware.authenticate_user import authenticate_user

#----------------------------------------------------------------------------------------------
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#----------------------------------------------------------------------------------------------
# Retorna todos los roles
@router.get("/")
async def get_all_roles_data(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(authenticate_user)):
    try:
        roles = get_all_rol(db, skip=skip, limit=limit)
        if not roles:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No roles found in the database."
            )

        # Procesar los valores antes de incluirlos en la respuesta
        rol_dicts = [
            {
                'id': rol.id,
                'name': rol.name,
                'ability': rol.ability
            }
            for rol in roles
        ]

        return Response(status="Ok", code="200", message="successfully", result = rol_dicts)

    except Exception as e:
        # Manejar la excepción aquí (puedes personalizar el mensaje de error)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving rol data: {str(e)}"
        )
       
#----------------------------------------------------------------------------------------------       
# Retorna un rol específico por ID
@router.get("/{rol_id}")

async def get_single_user(rol_id: int, db: Session = Depends(get_db), token: str = Depends(authenticate_user)):
    try: 
        roles = get_rol(db, rol_id)
        rol_dicts = [
            {
                'id': roles.id,
                'name': roles.name,
                'ability': roles.ability
            }
        ]
              
        return Response(status="Ok",
                          code="200",
                          message="Rol search successfully", result = rol_dicts)
        
    except Exception as e:
        return Response(status="Error",
                          code="404",  
                          message=f"Rol search failed{str(e)}")

#----------------------------------------------------------------------------------------------
# Crear un rol
@router.post("/")
async def create_single_rol(body_data = Body(...), db: Session = Depends(get_db),token: str = Depends(authenticate_user)):
    try:
        create_rol(db, rol_data = body_data)
        return Response(status="Ok", 
                        code="200", 
                        message="created successfully").dict(exclude_none=True)
    except Exception as e:
        return Response(status="Error ", code="500", message=str(e)).dict(exclude_none=True)
    
#---------------------------------------------------------------------------------------------- 
# Actualizar un rol por ID
@router.put("/{rol_id}")
async def update_single_user(rol_id: int,  body_data= Body(...), db: Session = Depends(get_db), token: str = Depends(authenticate_user)):
    
    try:
        rol = update_rol(db, rol_id, rol_data = body_data)
        rol_dicts = [
            {
                'id': rol.id,
                'name': rol.name,
                'ability': rol.ability
            }
        ]
        
        return Response(status="Ok",
                          code="200",
                          message="Rol update successfully", result = rol_dicts)
        
    except Exception as e:
        return Response(status="Error",
                          code="404",  
                          message=f"Rol update failed{str(e)}")    
    
#----------------------------------------------------------------------------------------------  
# Eliminar un rol por ID
@router.delete("/{rol_id}")
async def delete_single_rol(rol_id: int, token: str = Depends(authenticate_user), db: Session = Depends(get_db)):
    try:
        delete_rol(db, rol_id)
        return Response(status="Ok",
                        code="200",
                        message="Rol deleted successfully")
    except HTTPException as e:
        # Handle HTTP exceptions raised by the middleware or your logic
        return e
    except Exception as e:
        # Handle other unexpected errors
        return Response(status="Error",
                        code="404",
                        message=f"Rol deletion failed: {str(e)}")
