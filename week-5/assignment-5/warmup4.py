# Warmup 4: FizzBuzz (1 to 30)
for n in range(1, 31):
    if n % 3 == 0 and n % 5 == 0:   # check the combined case first
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
