#Writing using "w" mode

with open("students.txt", "w") as file:
    file.write("Alice: 85\n")
    file.write("Bob: 92\n")
    file.write("Charlie: 78\n")

print("---Initial 3 records written successfully---")


#append using "a" mode
with open("students.txt", "a") as file:
    file.write("David: 90\n")

print("---Fourth record appended successfully---")

#read the files and print it to terminal
print("\n---Reading data from students.txt: ---")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())


#Function

def read_file(filename):

    try:
        with open(filename, "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



#function test with correct filename
print("\n---Testing read file() with correct filename---")
read_file("students.txt")


#function test with incorrect filename
print("\n---Testing read_file() with wrong filename---")
read_file("missing_file.txt")


#Error Handling
try:
    marks = int(input("Enter marks: "))
    print(f"You entered: {marks}")

except ValueError:
    print("Please enter numbers only.")