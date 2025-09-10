from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nome_usuario: str
    email: str
    apelido_steam: str
    id_perfil: int

class UsuarioCreate(UsuarioBase):
    senha_usuario: str

class UsuarioUpdate(BaseModel):
    nome_usuario: Optional[str] = None
    email: Optional[str] = None
    senha_usuario: Optional[str] = None
    apelido_steam: Optional[str] = None
    id_perfil: Optional[int] = None

class Usuario(UsuarioBase):
    id_usuario: int
    data_criacao: datetime
    ultimo_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UsuarioLogin(BaseModel):
    email: str
    senha_usuario: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    nome_usuario: str
    email: str
    apelido_steam: str
    id_perfil: int
    data_criacao: datetime
    ultimo_login: Optional[datetime] = None
    
    class Config:
        from_attributes = True
