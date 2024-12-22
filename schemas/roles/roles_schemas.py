from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar

T = TypeVar('T')

class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T] = None  
    
class Ability(BaseModel):
    read: bool
    write: bool
    edit: bool
    delete: bool    
    
class RolSchema(BaseModel):
    name: str
    ability: Ability  

class RequestRol(BaseModel):
    parameter: RolSchema = Field(...)
