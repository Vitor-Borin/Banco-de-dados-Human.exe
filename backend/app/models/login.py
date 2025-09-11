from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoginBase(BaseModel):
    ip_login: str
    user_agent: str
    id_usuario: int

class LoginCreate(LoginBase):
    pass

class Login(LoginBase):
    id_login: int
    data_login: datetime
    
    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    id_login: int
    ip_login: str
    user_agent: str
    data_login: datetime
    id_usuario: int
    
    class Config:
        from_attributes = True
