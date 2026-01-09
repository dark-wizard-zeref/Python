# map: apply function to every item and return new iterable
# syntax: map(function, iterable)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}\n")

# filter: filter items based on a condition
# syntax: filter(function, iterable)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}\n")

# zip: combine multiple iterables into pair of elemets
# syntax: zip(iterable1, iterable2, ...)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped names and ages: {zipped}\n")