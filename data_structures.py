def main():
    # --- Section 1: Lists ---
    print("=== Section 1: Lists (Operations & Slicing) ===")
    marks = [85, 90, 78, 92, 88]
    print(f"Original marks: {marks}")

    marks.append(95)
    print(f"After adding 95: {marks}")

    marks.remove(78) 
    print(f"After removing 78: {marks}")

    marks.sort()
    print(f"Sorted marks: {marks}")

    sliced_marks = marks[1:4]
    print(f"Sliced marks (index 1 to 3): {sliced_marks}\n")

    # --- Section 2: Tuples ---
    print("=== Section 2: Tuples (Immutability & Unpacking) ===")
    coordinate = (10, 20)
    print(f"Coordinate tuple: {coordinate}")

    x, y = coordinate  # Unpack into variables
    print(f"Unpacked variables -> x: {x}, y: {y}")

    try:
        print("Attempting to modify coordinate[0]...")
        coordinate[0] = 15  # Tuples are immutable
    except TypeError as e:
        print(f"Caught expected TypeError: {e}\n")

    # --- Section 3: Sets ---
    print("=== Section 3: Sets (Uniqueness & Set Operations) ===")
    duplicate_list = [1, 2, 2, 3, 3, 3]
    unique_set = set(duplicate_list)
    print(f"Original list with duplicates: {duplicate_list}")
    print(f"Converted to set: {unique_set}")

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print(f"Set A: {set_a} | Set B: {set_b}")
    print(f"Union (A | B): {set_a.union(set_b)}")
    print(f"Intersection (A & B): {set_a.intersection(set_b)}")
    print(f"Difference (A - B): {set_a.difference(set_b)}\n")

    # --- Section 4: Dictionaries ---
    print("=== Section 4: Dictionaries (Key-Value Storage & Methods) ===")
    student = {"name": "Alice", "age": 20, "major": "Computer Science"}
    print(f"Initial student dictionary: {student}")

    student["gpa"] = 3.8  # Add a new key-value pair
    print(f"After adding 'gpa': {student}")

    student["age"] = 21  # Update an existing key
    print(f"After updating 'age': {student}")

    missing_grade = student.get("grade", "Not Available")  # Use .get() for missing key
    print(f"Using .get() for missing 'grade': {missing_grade}")

    print("Looping through dictionary .items():")
    for key, value in student.items():
        print(f"  - {key}: {value}")
    print()


if __name__ == "__main__":
    main()