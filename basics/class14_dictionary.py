d = {10: 101, 8: 64, 9: 81, 11: 121}

# access value using key
print(f"square of 10: {d[10]}\n")

# dictionary values are mutable
# dictionary keys are immutable
d[10] = 100

# keys must be unique
# values can be duplicated

# creating dictionary using dict()
dict_1 = dict(name="Achyut", age=22, profession="Student")
print(dict_1, "\n")

dict_2 = dict([
    ('name', 'Zeref'),
    ('age', 22),
    ('profession', 'Wizard')
])
print(dict_2, "\n")

# traversing dictionary
dict_3 = {10: 100, 20: 200, 30: 300, 40: 400, 50: 500}

# iterating over keys (default)
for key in dict_3:
    print(key, end=" ")
print("\n")

# iterating over values
for value in dict_3.values():
    print(value, end=" ")
print("\n")

"""
d.keys()       -> returns all keys
d.values()     -> returns all values
d.items()      -> returns (key, value) pairs as tuples
d.pop(key)     -> removes specified key and returns its value
d.popitem()    -> removes and returns the last (key, value) pair
d.update(a)    -> updates dictionary using another dictionary
                  (existing keys get overwritten)
"""

a = {10: 100, 20: 200, 30: 300}
b = {30: 3000, 40: 400, 50: 500}

# update dictionary
a.update(b)
print(a)