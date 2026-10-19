#Variables, data types, control structures (if/else, loops)


#Variables plus Data types
details = {
    "name" : "Hamza",
    "age" : 22,
    "class" : "CS",
    "marks" : [5,6,94,78,98]
}

#Type Check
print(type(details))
print(details["name"] , type(details["name"]))
print(type(details["age"]))
print(type(details["marks"]))


#For loop
for i in details["marks"]:    
    print(i)


avg = sum(details["marks"]) / len(details["marks"])
print("Average = " , avg)


#Control Structure
if avg >= 90 and avg <= 100:
    print("Grade A")

elif avg >= 80 and avg <90:
    print("Grade B")

elif avg >=70 and avg < 80:
    print("Grade C")

elif avg >= 60 and avg < 70:
    print("Grade D")

else:
    print("Fail!")


#While loop
while True:
    user_input =input("Enter a number {or type 'quit' to exit} ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        number = float(user_input)
        print(f"You Entered the number:  {number}")

    except ValueError:
        print("That is not a valid number. Please try again.")