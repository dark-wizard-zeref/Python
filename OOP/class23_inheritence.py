# Types of Inheritence Notes at the end
class Animal:
    # Parent / Base / Super class
    # -> Anything common to all animals goes here (shared attributes + shared behavior)
    def __init__(self, name, age):
        self.name = name  # instance attribute (belongs to object)
        self.age = age

    def info(self):
        # common method available to all child classes unless overridden
        print(f"Your name: {self.name} & Your age: {self.age}")


class Human(Animal):
    # Child / Derived / Sub class
    # -> Human IS-A Animal (Human inherits Animal)
    def __init__(self, name, age, num, group):      # super() calls the parent class constructor
                                              # -> this avoids repeating name/age assignment code
        super().__init__(name, age)
        self.num = num      
        self.group = group  


class Robot(Human):
    # Multi-level inheritance example:
    # Robot -> Human -> Animal
    # Robot indirectly gets Animal attributes too (name, age)
    def __init__(self, name, age, num, group, imei):
        super().__init__(name, age, num, group)
        self.imei = imei  # robot-specific attribute


class AI:
    # Separate class, not connected to Animal/Human chain
    def __init__(self, model):
        self.model = model


class Terminator(AI, Animal):
    def __init__(self, model, name, age):
        # Explicitly calling both parent constructors (simple + clear)
        AI.__init__(self, model)
        Animal.__init__(self, name, age)
    """
        Multiple inheritance:
        Terminator inherits from BOTH AI and Animal

        IMPORTANT:
        - Python uses MRO (Method Resolution Order) to decide which parent to use first
        - Since AI is first, Python searches AI before Animal for methods/constructors

        BUT:
        If we do `pass`, it inherits methods but doesn't automatically initialize attributes
        unless we define __init__ properly.
    """



obj1 = Animal("Lion", 12)
obj2 = Human("Zeref", 99, 8795694569, "B+")
obj3 = Robot("RoboZeref", 99, 8795694569, "B+", "IMEI-123456")
obj4 = Terminator("Skynet-v1", "T-800", 45)

# Example usage:
obj1.info()  # works (Animal has info)
obj2.info()  # works (Human inherits info from Animal)
obj3.info()  # works (Robot inherits info through Human -> Animal)

print(obj4.model)  # Terminator got AI stuff
obj4.info()        # Terminator got Animal stuff


"""
    1) Single level Inheritance:
    - One parent -> one child
    - Example: Human(Animal)
    - Human gets: name, age, info() from Animal
    - Human adds: num, group

    2) Multi level Inheritance:
    - A chain of inheritance (grandparent -> parent -> child)
    - Example: Robot(Human) and Human(Animal)
    - Robot gets:
            from Human: num, group
            from Animal: name, age, info()
    - Basically: Robot IS-A Human AND IS-A Animal

    3) Multiple Inheritance:
    - One child class inherits from multiple parents
    - Example: Terminator(AI, Animal)
    - Terminator can have:
            AI features (model)
            Animal features (name, age, info())
    - Python decides priority using MRO:
            Terminator -> AI -> Animal -> object
        So if both parents had the same method name, AI's version would win.

    4) Hierarchical Inheritance:
    - One parent -> multiple children
    - Example idea:
            class Dog(Animal)
            class Cat(Animal)
            class Human(Animal)
    - All share Animal features but each child adds its own stuff

    You should know:

    MRO/ Method Resolution Order = the order Python checks classes when searching for a method/attribute 
    (important in multiple inheritance)
    in MRO [ Terminator -> AI -> Animal -> object ]
    super() = calls the "next parent" based on that order

    In multiple inheritance:
    super() may only call ONE parent's __init__ first (depending on MRO),
    so sometimes we manually call both parent constructors to be sure everything initializes.

"""