from pydantic import BaseModel, ValidationError, Field

class Student(BaseModel):
    name: str
    age: int
    marks: list[int]


if __name__ == "__main__":

    student = Student(name= "Hamza", age=22, marks=[88, 92, 79, 95])

    print("Student Dictionary Dump:")
    print(student.model_dump())


    try:
        invalid_student = Student(name= "Ahmad", age= "abc", marks=[80,90])

    except ValidationError as e:

        print("Validation Error caught successfully!")
        print("-" * 40)
        print(e)
        print("-" * 40)


#Field (ge=0, le=100)

class ExamResult(BaseModel):
    student_name: str

    score: int = Field(ge=0, le=100, description= "Score must be between 0 and 100")


if __name__ == "__main__":
    print("Testing Pydantic field constraints (score between 0 and 100)...\n")


#Test 1
    try:
        print("Attempting to create a result with score = 150...")
        invalid_result = ExamResult(student_name="Hamza", score=150)

    except ValidationError as e:
        print("\n[Success] Validation Error caught for score=150:")
        print ("-" * 50)
        print(e)
        print ("-" * 50)

    print("\n" + "="*50 + "\n")


    #Test 2

    try:
        print("Attempting to create a result with score=85...")
        valid_result = ExamResult(student_name= "Ali", score = 85)
        print(f"\n[SUCCESS] Valid result created: {valid_result}")

    except ValidationError as e:
        print(e)