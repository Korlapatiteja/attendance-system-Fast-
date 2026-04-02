from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import model, sechma
from database import SessionLocal, Base, engine
import uvicorn
from auth import hash_password, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add_user")
def create_user(user: sechma.UserCreate, db: Session = Depends(get_db)):
    new_user = model.password(
        name=user.name,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@app.post("/login")
def login(user: sechma.login, db: Session = Depends(get_db)):
    db_user = db.query(model.password).filter(model.password.name == user.name).first()
    if not db_user:
        return {"message": "user not found"}
    if not verify_password(user.password, db_user.password):
        return {"message": "Invalid credentials"}
    return {"message": "login successful", "role": db_user.role}

@app.post("/add_student")
def add_student(student: sechma.students, db: Session = Depends(get_db)):
    existing = db.query(model.student).filter(model.student.roll_number == student.roll_number).first()
    if existing:
        return {"message": "Student with this roll number already exists"}
    new_student = model.student(roll_number=student.roll_number, name=student.name)
    db.add(new_student)
    new_user = model.password(name=student.name, password=hash_password(student.password), role="student")
    db.add(new_user)
    db.commit()
    return {"message": "Student added successfully"}

@app.post("/add_faculty")
def add_faculty(faculty: sechma.facultys, db: Session = Depends(get_db)):
    new_faculty = model.faculty(name=faculty.name, department=faculty.department)
    db.add(new_faculty)
    new_user = model.password(name=faculty.name, password=hash_password(faculty.password), role="faculty")
    db.add(new_user)
    db.commit()
    return {"message": "Faculty added successfully"}

@app.get("/get_students")
def get_students(db: Session = Depends(get_db)):
    return db.query(model.student).all()

@app.post("/mark_attendance")
def mark_attendance(user: sechma.attendance, db: Session = Depends(get_db)):
    if user.total_class <= 0:
        return {"message": "Total classes must be greater than zero"}
    if user.attended >= user.total_class:
        return {"message": "Attended classes cannot be greater than total classes"}

    percentage = (user.attended / user.total_class) * 100
    new_attendance = model.attendance(
        roll_number=user.roll_number,
        name=user.name,
        subject=user.subject,
        total_class=user.total_class,
        attended=user.attended,
        percentage=percentage
    )
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return {"message": "Attendance marked successfully"}

@app.get("/get_attendance/{roll_number}")
def get_attendance(roll_number: int, db: Session = Depends(get_db)):
    return db.query(model.attendance).filter(model.attendance.roll_number == roll_number).all()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
