from sqlalchemy.orm import Session
from models.rol.rol_model import Role
from schemas.roles.roles_schemas import RolSchema
from pydantic.main import BaseModel
import json

#-------------------------------------------------------------------------------------------
#todos los roles
def get_all_rol(db: Session, skip: int = 0, limit: int = 100):
    roles = db.query(Role).offset(skip).limit(limit).all()
    return roles

#-------------------------------------------------------------------------------------------
#un rol por id
def get_rol(db: Session, rol_id: int):
    rol = db.query(Role).filter(Role.id == rol_id).first()
    return rol

#-------------------------------------------------------------------------------------------
#creamos rol
def create_rol(db: Session, rol_data: RolSchema):
   
    name = rol_data['name']
    name_json = json.dumps(name)
    ability_json  = rol_data['ability']
 
    _Role = Role(
        name = name_json.strip('"'),
        ability = ability_json,
    )
    
    db.add(_Role)
    db.commit()
    db.refresh(_Role)
    return _Role

#-------------------------------------------------------------------------------------------
#actualizamos rol 
def update_rol(db: Session, rol_id: int, rol_data: RolSchema):

    rol = get_rol(db=db, rol_id=rol_id)

    if not rol:
        return None  # Rol no encontrado
    
    rol.name = rol_data.name if rol_data.name else rol.name
    rol.ability = rol_data.ability.model_dump() if rol_data.ability else rol.ability

    db.add(rol)
    db.commit()
    db.refresh(rol)

    return rol

#-------------------------------------------------------------------------------------------
#eliminar rol por id
def delete_rol(db: Session, rol_id: int) -> bool:
    rol_to_delete = get_rol(db=db, rol_id=rol_id)
    if rol_to_delete is None:
        return False
    db.delete(rol_to_delete)
    db.commit()

    return True

