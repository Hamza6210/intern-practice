from pydantic import BaseModel

class Student(BaseModel):
    name: str
    marks: int

student = Student(name="Hamza", marks=90)
print("Hello from the container", student.model_dump())