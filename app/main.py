from typing import List
import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud_estudiante as estu, models, schemas
from . import crud_curso  as curs
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/v1/estudiantes/", response_model=schemas.Estudiante)
def create_estudiante(estudiante: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return estu.create_estudiante(db=db, estudiante=estudiante)




@app.get("/api/v1/estudiantes/{estudiante_id}", response_model=schemas.Estudiante)
def read_estudiante(estudiante_id: int, db: Session = Depends(get_db)):
    db_estudiante = estu.get_estudiante(db, estudiante_id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante not found")
    return db_estudiante


@app.post("/api/v1/estudiantes/login", response_model=schemas.Estudiante)
def login(credenciales: schemas.EstudianteLogin, db: Session = Depends(get_db)):
    db_estudiante = estu.login(db, credenciales= credenciales)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado, validar credenciales!")
    return db_estudiante

@app.put("/api/v1/estudiantes/{estudiante_id}", response_model=schemas.Estudiante)
def put_estudiante(estudiante_id: int,estudiante: schemas.EstudianteCreate, db:Session = Depends(get_db)):
    db_estudiante = estu.get_estudiante(db, estudiante_id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")
    else:
        db_estudiante=estu.put_estudiante(db,estudiante_id=estudiante_id,estudiante=estudiante)
    return db_estudiante

@app.delete("/api/v1/estudiantes/{estudiante_id}")
def delete_estudiante(estudiante_id: int, db:Session = Depends(get_db)):

    db_estudiante = estu.get_estudiante(db, estudiante_id=estudiante_id)
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Estudiante not found")
    else:
        estu.delete_estudiante(db,estudiante_id=estudiante_id)
        return {"ok":'Estudiante Deleted'}
     


@app.get("/api/v1/estudiantes/", response_model=List[schemas.Estudiante])
def read_estudiantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudiantes = estu.get_estudiantes(db, skip=skip, limit=limit)
    return estudiantes


##---- cursos

@app.post("/api/v1/cursos/", response_model=schemas.Curso)
def create_curso(curso: schemas.CursoCreate, db: Session = Depends(get_db)):
    print(curso)
    db_curso= curs.get_curso_letra_numero(db,curso.letra,curso.numero)
    if db_curso is None:
        return curs.create_curso(db=db, curso=curso)
    else:
        raise HTTPException(status_code=404, detail="Curso ya está registrado!")



@app.get("/api/v1/cursos/{curso_id}", response_model=schemas.Curso)
def read_curso(curso_id: int, db: Session = Depends(get_db)):
    db_curso = curs.get_curso(db, curso_id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso no encontrado!")
    return db_curso

@app.get("/api/v1/cursos/", response_model=List[schemas.Curso])
def read_cursos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cursos = curs.get_cursos(db, skip=skip, limit=limit)
    return cursos

