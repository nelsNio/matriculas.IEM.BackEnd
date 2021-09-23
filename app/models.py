from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,Enum
from sqlalchemy.orm import relationship

from .database import Base



class Estudiante(Base):
    __tablename__ = "estudiantes"
    id = Column(Integer, primary_key=True, index=True)
    fecha_insercion = Column(Date, index=False, default=datetime.now())
    primer_nombre = Column(String, index=False,nullable=False)
    segundo_nombre = Column(String, index=False,nullable=False)
    primer_apellido = Column(String, index=False,nullable=False)
    segundo_apellido= Column(String, index=False,nullable=False)
    documento_identidad = Column(Enum('CC','TI',name='tipos_documentos'), index=False)
    numero_documento = Column(Integer, index=True, unique=True)
    contrasenia= Column(String, index=False,nullable=False)
    e_mail= Column(String, index=False,nullable=False)

