#File reader as in I/O

def read_file():
    print("==============================")
    print("      SIMPLE FILE READER")
    print("==============================")
    
    filename = input("Enter the filename to read: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()

        print(f"\n--- Contents of '{filename}' ---")
        for index, line in enumerate(lines, start=1):
            # Print with line numbers, using rstrip to avoid double spacing
            print(f"{index:3} | {line.rstrip()}")

        print("-" * (len(filename) + 20))
        print(f" Total line count: {len(lines)}\n")

    except FileNotFoundError:
        print(f" Friendly Error: Oops! We couldn't find a file named '{filename}'. Please check the spelling or path and try again.\n")
    except PermissionError:
        print(f" Friendly Error: You don't have permission to read '{filename}'.\n")
    except Exception as e:
        print(f" An unexpected error occurred: {e}\n")


if __name__ == "__main__":
    read_file()