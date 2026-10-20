#Type hinting
def calculate_average(marks: list[int]) -> float:

    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def greet(name: str = "Guest") -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":

    sample_marks = [85, 90, 78, 92, 88]
    avg = calculate_average(sample_marks)

    print(f"Marks: {sample_marks}")
    print(f"Average: {avg:.2f}")

    print(greet("Hamza"))
    print(greet())