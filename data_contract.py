from pydantic import BaseModel, ConfigDict, Field, ValidationError

class StudentRecord(BaseModel):

    model_config = ConfigDict(strict=True, extra="forbid")

    name: str = Field(min_length=2)
    age: int = Field(ge=15, le=60)
    score: float = Field(ge=0, le=100)


if __name__ == "__main__":
    print("=== Testing Pydantic Data Contract & Strict Mode ===\n")

    try:
        valid_data = {"name": "Ali", "age": 22, "score": 86.5}
        student = StudentRecord.model_validate(valid_data)
        print("[SUCCESS] Valid record passed:", student.model_dump())

    except ValidationError as e:
        print("[ERROR] Valid record failed unexpectedly:", e)

    print("-" * 60)


    try:
        invalid_age_data = {"name": "Ali", "age": "22", "score": 85.5}
        StudentRecord.model_validate(invalid_age_data)
    except ValidationError as e:
        print("[CAUGHT] Strict mode correctly rejected string age ('22'):")
        print(f" -> {e.errors()[0]['msg']}")

    print("-" * 60)


    try:
        extra_field_data = {"name": "Ali", "age": 22, "score": 85.5, "city": "Lahore"}
        StudentRecord.model_validate(extra_field_data)
    except ValidationError as e:
        print("[CAUGHT] Extra forbid rule correctly rejected extra field ('city'):")
        print(f" -> {e.errors()[0]['msg']}")

    print("-" * 60)


    try:
        invalid_score_data = {"name": "Ali", "age": 22, "score": 150.0}
        StudentRecord.model_validate(invalid_score_data)
    except ValidationError as e:
        print("[CAUGHT] Range rule correctly rejected score out of bounds (150.0):")
        print(f" -> {e.errors()[0]['msg']}")


    