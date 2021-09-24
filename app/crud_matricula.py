from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from .models import Matricula



from . import models, schemas

def get_matricula(db: Session, matricula_id: int):
    return db.query(Matricula).filter(Matricula.id == matricula_id).first()

def read_estudiante_matriculas(db: Session, estudiante_id: int):
    print(estudiante_id)
    return db.query(Matricula).filter(Matricula.estudiante_id == estudiante_id).all()


def delete_matricula(db: Session, matricula_id: int):
    db.query(Matricula).filter(Matricula.id == matricula_id).delete()
    db.commit()


def get_matriculas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Matricula).offset(skip).limit(limit).all()


def create_matricula(db: Session, matricula: schemas.MatriculaCreate):
    db_matricula = Matricula(**matricula.dict())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula



