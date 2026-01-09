a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension: concise way to create lists
even = [x for x in a if x % 2 == 0]
print(f"Even numbers: {even}\n")

# set comprehension: create sets with unique elements
odd = {x for x in a if x % 2 != 0}
print(f"Odd numbers: {odd}\n")

# dictionary comprehension: create dictionaries
squares = {x: x**2 for x in a}
print(f"Squares: {squares}\n")