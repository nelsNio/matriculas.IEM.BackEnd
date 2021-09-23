from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from fastapi.encoders import jsonable_encoder
from .models import Estudiante


from . import models, schemas

def get_estudiante(db: Session, estudiante_id: int):
    return db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()

def put_estudiante(db: Session, estudiante_id: int,  estudiante: schemas.EstudianteCreate):

    """

    db
    estudiante_id
    """
    estudiante_upd=estudiante.dict()
    db_estudiante =db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).first()
    db.query(models.Estudiante).filter(models.Estudiante.id == estudiante_id).update(estudiante_upd,'fetch')
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

def delete_estudiante(db: Session, estudiante_id: int):
    db.query(Estudiante).filter(Estudiante.id == estudiante_id).delete()
    db.commit()


def get_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estudiante).offset(skip).limit(limit).all()


def create_estudiante(db: Session, estudiante: schemas.EstudianteCreate):
    db_estudiante = models.Estudiante(**estudiante.dict())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante



