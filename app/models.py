from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Numeric


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
    matricula = relationship("Matricula", back_populates="estudiante")





class Matricula(Base):
    __tablename__ = "matricula"
    id = Column(Integer, primary_key=True, index=True)
    
    estudiante_id= Column(Integer, ForeignKey("estudiantes.id"))
    estudiante= relationship("Estudiante", back_populates="matricula")

    curso_id= Column(Integer, ForeignKey("cursos.id"))
    curso = relationship("Curso", back_populates="matricula")

    

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Numeric, index=False,nullable=False)
    letra = Column(String, index=False,nullable=False)
    alias = Column(String, index=False,nullable=False)
    matricula = relationship("Matricula", back_populates="curso")


 
