# Warmup 2: Input Validation with a While Loop
while True:
    entry = input("Enter a positive integer: ")

    try:
        value = int(entry)          # raises ValueError for text like "hello"
    except ValueError:
        print("That's not a positive integer. Try again.")
        continue                    # skip the rest and ask again

    if value > 0:
        print(f"Got it: {value}")
        break                       # valid input, so stop the loop
    else:
        print("That's not a positive integer. Try again.")
