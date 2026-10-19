#import helpers
from mypackage.helpers import calculate_average, get_grade, greet


#average Function called
student5 = [71, 94, 82,]
avg5 = calculate_average(student5)

student6 = [19, 82, 73, 49, 95]
avg6 = calculate_average(student6)

print(avg5)
print(avg6)


#Grade Function called
grade5 = get_grade(avg5)
grade6 = get_grade(avg6)

print(f"Student 5: {grade5}")
print(f"Student 6: {grade6}")

#Greet Function called

greet("Hamza") 
greet()