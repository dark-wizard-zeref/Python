"""
functions
A function is a block of reusable code that performs a specific task.
Functions help reduce code repetition and improve readability.

parameters = while defining function
arguments = while calling function
"""
# syntax:
# def function_name(parameters):
#     code
#     return value (optional)

# Example 1: function without parameters
def greet():
    print("Hello!")

greet()  # function call

print()

# Example 2: function with parameters
def greet_person(name):
    print("Hello", name)

greet_person("Achyut")

print()

# Example 3: function with return value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

print()

# Example 4: default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(5))     # uses default exponent
print(power(2, 3))  # overrides default

print()

# Example 5: function with multiple return values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

s, d = calculate(10, 5)
print(s, d)

# *args and **kwargs
# They allow a function to accept a variable number of arguments.

# *args (Non-keyword / positional arguments)
# Stores extra positional arguments as a tuple

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))

print()

# **kwargs (Keyword arguments)
# Stores extra keyword arguments as a dictionary

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_details(name="Achyut", age=21, course="AI")

print()

# Using *args and **kwargs together
def demo(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

demo(1, 2, 3, 4, x=10, y=20)