"""
Abstraction = hide unnecessary details, show only what is important

- We force all subclasses to follow a common rule/interface
- Parent class decides WHAT method must exist
- Child class decides HOW it will work

Abstract Class:
- A class that contains at least 1 abstract method
- You cannot create object of an abstract class

Abstract Method:
- A method that is declared but not written (no real code)
- Every subclass MUST implement it
"""

# abc module is used for abstraction in Python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        # abstract method (only name is given, no implementation)
        # any class inheriting Animal must implement sound()
        pass


class Dog(Animal):
    def sound(self):
        # implementation of abstract method
        print("hello, I bark")


# Dog works because it implemented sound()
dog = Dog()
dog.sound()

# Animal won't work:
# a = Animal()  
# ERROR: Can't instantiate abstract class Animal 
# without an implementation for abstract method 'sound'