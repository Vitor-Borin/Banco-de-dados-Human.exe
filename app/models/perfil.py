from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PerfilBase(BaseModel):
    nome_perfil: str
    desc_perfil: str

class PerfilCreate(PerfilBase):
    pass

class PerfilUpdate(BaseModel):
    nome_perfil: Optional[str] = None
    desc_perfil: Optional[str] = None

class Perfil(PerfilBase):
    id_perfil: int
    
    class Config:
        from_attributes = True
