from pydantic import BaseModel, Field
from typing import Optional,  TypeVar


T = TypeVar('T')

class Response(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None  
    
    
class Ability(BaseModel):
    read: bool
    write: bool
    edit: bool
    delete: bool

class UserSchema(BaseModel):
    full_name: str
    username: str
    email: str
    password: str
    phone: int
    rol_id:int

class EmailSchema(BaseModel):
    email: str
    password: str
    
class New_userSchema(BaseModel):
    template: str
    name: str 
    email: str
    password: str  
       
class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)