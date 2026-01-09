def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.\n")
    return wrapper


@my_decorator   # this means say_hello will be passed to my_decorator as an argument
def say_hello():
    print("Hello!")


say_hello()
# A decorator is a special type of function that:
#   - Takes another function as an argument
#   - Extends or alters its behavior without modifying its code

def decorate(func):
    def wrapper(a,b):
        print("Starting the function...")
        result = func(a,b)
        print("Function has ended.\n")
        return result
    return wrapper


@decorate
def add(x, y):
    print(f"The sum is: {x + y}")


add(5, 7)