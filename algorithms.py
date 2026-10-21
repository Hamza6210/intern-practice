def linear_search(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index

    return -1



def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

def bubble_sort(items):
    arr = list(items)
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
            
    return arr 


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursively calculates the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    # --- Section 1: Searching Algorithms ---
    print("=== Section 1: Searching Algorithms ===")
    sorted_numbers = [10, 22, 35, 47, 59, 63, 88, 91]
    target = 47
    
    print(f"Sorted list: {sorted_numbers}")
    print(f"Target to find: {target}")

    linear_idx = linear_search(sorted_numbers, target)
    binary_idx = binary_search(sorted_numbers, target)

    print(f"Linear Search index: {linear_idx}")
    print(f"Binary Search index: {binary_idx}\n")

    # --- Section 2: Sorting Algorithm ---
    print("=== Section 2: Sorting Algorithm (Bubble Sort) ===")
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted list: {unsorted_numbers}")

    sorted_result = bubble_sort(unsorted_numbers)
    expected_result = sorted(unsorted_numbers)

    print(f"Bubble Sorted: {sorted_result}")
    print(f"Matches Python's built-in sorted(): {sorted_result == expected_result}\n")

    # --- Section 3: Recursive Functions ---
    print("=== Section 3: Recursive Functions ===")
    
    num = 5
    fact_result = factorial(num)
    print(f"Factorial of {num} (5!): {fact_result}")

    fib_index = 7
    fib_result = fibonacci(fib_index)
    print(f"Fibonacci number at index {fib_index}: {fib_result}\n")


if __name__ == "__main__":
    main()