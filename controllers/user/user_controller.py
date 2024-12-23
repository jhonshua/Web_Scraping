from sqlalchemy.orm import Session
from models.user.user_model import User
from schemas.user.user_schemas import EmailSchema, UserSchema, New_userSchema
from utils.helper_functions import get_password_hash

#Todos los usuarios.
from sqlalchemy import or_

def get_all_users(db: Session, 
                  skip: int = 0, 
                  limit: int = 100, 
                  sort: str = "asc", 
                  full_name: str = None):

    query = db.query(User)

    # Si se proporciona un término de búsqueda, filtramos por nombre completo
    if full_name:
        query = query.filter(User.full_name.ilike(f"%{full_name}%"))

    # Ordenamos los resultados según el criterio especificado
    if sort:
        if sort == "asc":
            query = query.order_by(User.full_name.asc())
        elif sort == "desc":
            query.order_by(User.full_name.desc())

    # Aplicamos paginación
    return query.offset(skip).limit(limit).all()



#Un usuario por ID.
def get_user(db: Session, user_id: int):
     return db.query(User).filter(User.id == user_id).first()
 
 
#Creamos usuario.
def create_user(db: Session, user_data: UserSchema):
    _User = User(
        full_name = user_data.full_name,
        username = user_data.username,
        email = user_data.email,
        password = get_password_hash(user_data.password) ,
        phone=user_data.phone,
        rol_id=user_data.rol_id,
    )
    
    db.add(_User)
    db.commit()
    db.refresh(_User) 
    
    return _User

 
#Actualizamos usuario.
def update_user(db: Session, user_id: int, user_data: UserSchema):
    
    
    user = get_user(db=db, user_id=user_id)
    if not user:
        return None
    if not user_data:
        return None  
    user.full_name = user_data.full_name if user_data.full_name is not None else user.full_name
    user.username = user_data.username if user_data.username is not None else user.username
    user.email = user_data.email if user_data.email is not None else user.email
    user.password = get_password_hash(user_data.password) if user_data.password is not None else user.password
    user.phone = user_data.phone if user_data.phone is not None else user.phone
    user.rol_id = user_data.rol_id if user_data.rol_id is not None else user.rol_id

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
   

#Eliminamos usuario.
def delete_user(db: Session, user_id: int) -> bool:
    user_to_delete = get_user(db=db, user_id=user_id)
    if user_to_delete is None:
        return False
    db.delete(user_to_delete)
    db.commit()

    return True