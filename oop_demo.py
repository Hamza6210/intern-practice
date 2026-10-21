class  Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


    def average(self):

        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def get_grade(self):

        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def describe(self):
        return f"{self.name} is an undergraduate student."

    def __str__(self):
        return (
            f"Student: {self.name} | Age: {self.age} | "
            f"Average Marks: {self.average():.1f} | Grade: {self.get_grade()}"
        )


class Graduate(Student):
    def __init__(self, name, age, marks, degree):
        super().__init__(name, age, marks)
        self.degree = degree

    def describe(self):
        return f"{self.name} is a graduate student pursuing a {self.degree}."

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str} | Degree: {self.degree}"


def main():

    print("=== Section 1: Creating Student and Graduate Objects ===")
    student1 = Student("Alice Smith", 20, [88, 92, 85])
    student2 = Student("Bob Jones", 22, [70, 65, 75])
    grad1 = Graduate("Charlie Brown", 26, [95, 91, 94], "Master of Data Science")

    academic_roster = [student1, student2, grad1]
    print(f"Successfully created {len(academic_roster)} records. \n")


    print("=== Section 2: Roster Summary and Polymorphic Behavior ===")
    for person in academic_roster:
        print(person)

        print(f" -> Description: {person.describe()}")
        print("-" * 65)


if __name__ == "__main__":
    main()