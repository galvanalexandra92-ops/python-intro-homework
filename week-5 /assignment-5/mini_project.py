# Mini-Project: Number Cruncher

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def read_number(prompt):
    """Ask for a number; return None if the input isn't a number."""
    text = input(prompt)
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return None


def find_minimum(values):
    smallest = values[0]            # start with the first item as the "best so far"
    for v in values:
        if v < smallest:
            smallest = v
    return smallest


def find_maximum(values):
    largest = values[0]
    for v in values:
        if v > largest:
            largest = v
    return largest


def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1                       # not found


def bubble_sort(values):
    n = len(values)
    swapped = True
    while swapped:                  # keep making passes until a pass has no swaps
        swapped = False
        for i in range(n - 1):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = values[i + 1], values[i]   # swap
                swapped = True


while True:
    print()
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print(f"The minimum is {find_minimum(numbers)}.")
    elif choice == "2":
        print(f"The maximum is {find_maximum(numbers)}.")
    elif choice == "3":
        target = read_number("Enter a number to search for: ")
        if target is None:
            print("That's not a number.")
        else:
            index = linear_search(numbers, target)
            if index != -1:
                print(f"Found {target} at index {index}.")
            else:
                print(f"{target} was not found in the list.")
    elif choice == "4":
        bubble_sort(numbers)
        print(f"Sorted list: {numbers}")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please enter a number from 1 to 5.")
