# Warmup 3: Linear Search (no .index() and no `in` operator)
names = ["Camila", "Diego", "Valeria", "Marcus", "Sofia", "Andres", "Luz", "Mateo"]

target = input("Enter a name to search for: ")

found_at = -1                       # -1 means "not found yet"

for i in range(len(names)):
    if names[i] == target:
        found_at = i
        break                       # stop at the first match

if found_at != -1:
    print(f'Found "{target}" at index {found_at}.')
else:
    print(f'"{target}" was not found in the list.')
