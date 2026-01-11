# Exception Handling in Python
# This file shows common ways to handle errors so programs don't crash.

# 1. Basic try-except-else-finally

def basic_exception_handling():
    try:
        # Code that might cause an error
        result = 10 / 0
    except ZeroDivisionError:
        # Runs if division by zero happens
        print("Caught a division by zero error!")
    else:
        # Runs if no exception occurs
        print("Division successful, result is:", result)
    finally:
        # Always runs (error or not)
        print("Execution of basic_exception_handling complete.")


# 2. Handling more than one possible error
def multiple_exceptions_handling(): 
    try:
        # User input and division (both can fail)
        num = int(input("Enter a number: "))
        result = 10 / num
    except ZeroDivisionError:
        # Handles division by zero
        print("Caught a division by zero error!")
    except ValueError:
        # Handles invalid integer input
        print("Caught a value error! Please enter a valid integer.")
    else:
        # Runs if everything works
        print("Division successful, result is:", result)
    finally:
        # Always executes
        print("Execution of multiple_exceptions_handling complete.")


# 3. Manually raising an exception
def raise_exception_example():
    def check_positive(number):
        # Raise an error if condition is not met
        if number < 0:
            raise ValueError("Negative value provided!")
        return number

    try:
        check_positive(-5)
    except ValueError as ve:
        # Catch the manually raised error
        print("Caught an exception:", ve)
    finally:
        print("Execution of raise_exception_example complete.")


# 4. Creating and using a custom exception
class CustomError(Exception):
    """User-defined exception."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def custom_exception_handling():
    def trigger_custom_error(condition):
        # Raise custom error if condition is True
        if condition:
            raise CustomError("This is a custom error triggered!")
    
    try:
        trigger_custom_error(True)
    except CustomError as ce:
        # Catch custom exception
        print("Caught a custom exception:", ce)
    finally:
        print("Execution of custom_exception_handling complete.")


# Run all examples
if __name__ == "__main__":
    print("1. Basic Exception Handling:")
    basic_exception_handling()

    print("\n2. Multiple Exceptions Handling:")
    multiple_exceptions_handling()

    print("\n3. Raising Exceptions Example:")
    raise_exception_example()

    print("\n4. Custom Exception Handling:")
    custom_exception_handling()