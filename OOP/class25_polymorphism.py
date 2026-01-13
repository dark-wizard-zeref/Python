"""
Polymorphism: same name different functionality

~ It allows different classes to define method with same name but different behaviors
~ It is achieved through method overriding (when using inheritance)

Types of Polymorphism:
1) Method Overloading:
   - Same method name with different parameters
   - Python doesn't support traditional overloading like Java/C++

2) Method Overriding:
   - When subclass defines a method with same name as superclass
   - Child's method replaces parent's method for child objects
"""

class Animal:
    name = "lion"

    def speak(self):
        print("I roar")


class Bird(Animal):
    name = "sparrow"

    def speak(self):  # Method overriding (Bird replaces Animal's speak())
        print("I chirp")


obj = Animal()
obj1 = Bird()

obj.speak()   # runs Animal.speak()
obj1.speak()  # runs Bird.speak() because Bird overrides it