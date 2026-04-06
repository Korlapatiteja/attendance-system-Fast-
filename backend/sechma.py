from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str
    role: str

class login(BaseModel):
    name: str
    password: str

class students(BaseModel):
    roll_number: int
    name: str
    password: str

class facultys(BaseModel):
    name: str
    password: str
    department: str

class attendance(BaseModel):
    roll_number: int
    name: str
    subject: str
    total_class: int
    attended: int
    percentage: float
