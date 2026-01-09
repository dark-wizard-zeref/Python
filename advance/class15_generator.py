# A generator is a special kind of function that:
# - Produces values one at a time
# - Remembers where it left off between calls
# - Uses 'yield' instead of 'return'

def generator():
    # Loop from 0 to 4 (5 is not included)
    for i in range(5):
        # 'yield' pauses the function here
        # and returns the current value of i
        yield i


# Create a generator object (no code inside runs yet)
gen = generator()

# next() gets the next value from the generator
print(f"Generator first num: {next(gen)}\n")   # Output: 0

# Generator continues from where it stopped
print(f"Generator second num: {next(gen)}\n")  # Output: 1

# Convert remaining generator values into a list
# The generator is exhausted after this
print(f"Rest values: {list(gen)}\n") 

# Generators are memory efficient for large datasets

# Generator comprehension: similar to list comprehensions
gen_comp = (x * x for x in range(5)) # use parentheses () instead of brackets []
print(f"first num: {next(gen_comp)}")
print(f"second num: {next(gen_comp)}")
print(f"rest of them: {list(gen_comp)}\n")
