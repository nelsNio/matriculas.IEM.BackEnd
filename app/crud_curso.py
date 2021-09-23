from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import true
from .models import Curso



from . import models, schemas

def get_curso(db: Session, curso_id: int):
    return db.query(Curso).filter(Curso.id == curso_id).first()

def get_curso_letra_numero(db: Session, letra: str,numero:int):
    return db.query(Curso).filter(Curso.letra == letra, Curso.numero==numero).first()



def delete_curso(db: Session, curso_id: int):
    db.query(Curso).filter(Curso.id == curso_id).delete()
    db.commit()


def get_cursos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Curso).offset(skip).limit(limit).all()


def create_curso(db: Session, curso: schemas.CursoCreate):
    db_curso = Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso



