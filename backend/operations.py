from sqlalchemy.orm import Session
import model
import sechma

def create_user(db:Session,user:sechma.Usercreate):
    new_user=model.User(username=user.username,password=user.password,role=user.role) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def mark_attendance(db:Session,attendance:sechma.attendance_students):
    new_attendance=model.student(roll_number=attendance.roll_number,name=attendance.name,subject=attendance.subject,attend=attendance.attend,absent=attendance.absent,percentage=attendance.percentage)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

def get_attendance(db:Session,roll_number:int):
    return db.query(model.student).filter(model.student.roll_number==roll_number).first

def create_faculty(db:Session,faculty:sechma.faculty):
    new_faculty=model.faculty(name=faculty.name,department=faculty.department)
    db.add(new_faculty)
    db.commit()
    db.refresh(new_faculty)
    return new_faculty