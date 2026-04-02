from sqlalchemy import Column, Integer, String,Float
from database import Base

class password(Base):
    __tablename__ = "passwords"
    id= Column(Integer, primary_key=True, index=True)
    name = Column(String,unique=True,index=True)
    password = Column(String)
    role = Column(String)

class student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    roll_number = Column(Integer,unique=True,index=True)
    name = Column(String,unique=True,index=True)
    
class attendance(Base):
    __tablename__ ="attendance"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    roll_number = Column(Integer,unique=True,index=True)
    subject = Column(String)
    total_class=Column(Integer)
    attended=Column(Integer)
    percentage = Column(Float)

class faculty(Base):
    __tablename__ = "facultys"

    id = Column(Integer, primary_key=True, index=True)
    roll_number=Column(Integer,unique=True,index=True)
    name = Column(String,unique=True,index=True)
    department = Column(String)