from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db, engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class StudentCreate(BaseModel):
    reg_no: str
    name: str
    email: str


@app.get("/health")
def health():
    return {"status": "ok", "db": "connected", "student": "2212164"}


@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Student).filter(
        models.Student.reg_no == student.reg_no
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Student already exists")
    db_student = models.Student(
        reg_no=student.reg_no,
        name=student.name,
        email=student.email
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.get("/students/{reg_no}")
def get_student(reg_no: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.reg_no == reg_no
    ).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
