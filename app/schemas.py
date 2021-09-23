from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel

#---- ESQUEMA ESTUDIANTE
class EstudianteBase(BaseModel):
    primer_nombre : str
    segundo_nombre : str
    primer_apellido : str
    segundo_apellido: str
    documento_identidad : str
    numero_documento : int
    fecha_insercion:date=datetime.now()
    contrasenia:str
    e_mail:str

class EstudianteLogin(BaseModel):
    contrasenia:str
    e_mail:str


class EstudianteCreate(EstudianteBase):
    pass


class Estudiante(EstudianteBase):
    id: int

    class Config:
        orm_mode = True



#---- ESQUEMA ESTUDIANTE
class CursoBase(BaseModel):
    numero:int
    letra:str
    alias:str


class CursoCreate(CursoBase):
    pass


class Curso(CursoBase):
    id: int

    class Config:
        orm_mode = True
