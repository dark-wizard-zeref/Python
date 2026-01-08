# naming conventions
"""
1. camelCase
2. PascalCase
3. snake_case
"""

# data types
"""
1. Numeric: int, float, complex (2i, 5j)
2. String: 'achyut' or "achyut"
3. Boolean: True, False
"""

a = "action inaction and inaction in action"

# indexing
print(a[1], a[-2])

# strings are immutable
# slicing [start:stop(exclusive):step]
# [:] prints the whole string
print(a[:15], a[16:19], a[20:])

# formatted strings
print(f"Quote:\n{a}")
# \n is an escape sequence character

# raw strings
print(r"I'm Achyut\nMy age is 22")
# escape sequences do not work in raw strings

A = 22

# type conversion
print(f"before type conversion: {type(A)}")
A = str(A)
print(f"after type conversion: {type(A)}")

x = ""  # empty string

# boolean conversion
print(f"A to boolean: {bool(A)}")
print(f"x to boolean: {bool(x)}")

# falsy values
"""
0
0.0
False
""  (empty string)
[]  (empty list)
()  (empty tuple)
{}  (empty dictionary)

all other values are truthy
"""