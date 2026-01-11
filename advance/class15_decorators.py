# A decorator is a function that:
# - Takes another function as input
# - Adds extra behavior before or after that function
# - Does NOT change the original function’s code

def my_decorator(func):
    # This inner function wraps the original function
    def wrapper():
        # Code that runs BEFORE the original function
        print("Before the function is called.")

        # Call the original function
        func()

        # Code that runs AFTER the original function
        print("After the function is called.\n")

    # Return the wrapper function (not calling it)
    return wrapper


# Using @my_decorator is the same as:
# say_hello = my_decorator(say_hello)
@my_decorator
def say_hello():
    print("Hello!")


# Calling say_hello() actually calls wrapper()
say_hello()


# Decorator example WITH arguments and return values

def decorate(func):
    # Wrapper must accept the SAME parameters as the function
    def wrapper(a, b):
        # Code before the original function
        print("Starting the function...")

        # Call the original function and store its result
        result = func(a, b)

        # Code after the original function
        print("Function has ended.\n")

        # Return the original function’s result
        return result

    return wrapper


@decorate
def add(x, y):
    # Original function logic stays untouched
    print(f"The sum is: {x + y}")


# This calls wrapper(5, 7), not add() directly
add(5, 7)