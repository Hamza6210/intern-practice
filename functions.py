#Average Function
def calculate_average(marks):
    if not marks:
        return 0.0

    total = sum(marks)
    average = total / len(marks)
    return average

student1 = [85, 90, 78, 92, 88]
average = calculate_average(student1)
print(average)


# Grade Function
def get_grade(average):
    if average >= 90 and average <= 100:
        return "Grade A"
    elif average >= 80 and average < 90:
        return "Grade B"
    elif average >= 70 and average < 80:
        return "Grade C"
    elif average >= 60 and average < 70:
        return "Grade D"
    else:
        return "Fail!"  

grade = get_grade(average)
print(grade)


#Greet function
def greet(name = "Guest"):
    print(f"Hello, {name}!")

greet()