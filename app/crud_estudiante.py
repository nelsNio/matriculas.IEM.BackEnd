from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from .models import Estudiante



from . import models, schemas

def get_estudiante(db: Session, estudiante_id: int):
    return db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()


def login(db: Session, credenciales:schemas.EstudianteLogin):
    return db.query(Estudiante).filter(Estudiante.e_mail == credenciales.e_mail,Estudiante.contrasenia==credenciales.contrasenia).first()

def put_estudiante(db: Session, estudiante_id: int,  estudiante: schemas.EstudianteCreate):

    """

    db
    estudiante_id
    """
    estudiante_upd=estudiante.dict()
    db_estudiante =db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    db.query(Estudiante).filter(Estudiante.id == estudiante_id).update(estudiante_upd,'fetch')
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def delete_estudiante(db: Session, estudiante_id: int):
    db.query(Estudiante).filter(Estudiante.id == estudiante_id).delete()
    db.commit()


def get_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Estudiante).offset(skip).limit(limit).all()


def create_estudiante(db: Session, estudiante: schemas.EstudianteCreate):
    db_estudiante = Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante



