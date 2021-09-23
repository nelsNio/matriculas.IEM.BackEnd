from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class EstudianteBase(BaseModel):
    primer_nombre : str
    segundo_nombre : str
    primer_apellido : str
    segundo_apellido: str
    documento_identidad : str
    numero_documento : int
    fecha_insercion:date=datetime.now()




class EstudianteCreate(EstudianteBase):
    pass


class Estudiante(EstudianteBase):
    id: int

    class Config:
        orm_mode = True
