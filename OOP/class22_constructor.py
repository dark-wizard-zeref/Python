class Animal:
    gender = 'Male'
    # Class attribute: does not use self keyword
    # This belongs to the class itself, not to any single object
    # All objects of this class can access it

    def __init__(self, name, age):
        self.name = name    # Instance attributes: uses self keyword
        self.age = age      # These belong to a specific object
        
    def speak(self):
        """
        Instance method: uses self keyword as parameter
        Works with data of the object that calls it
        """
        print(f"{self.name} is talking...")

    @classmethod
    def clsmethod(cls):
        print(f"Sex: {cls.gender}")
        """
        Class method
        Uses 'cls' instead of 'self'

        'cls' refers to the class itself, not an object.
        cls points to class (in this case Animal)
        Used when we want to work with class only data.
        """

    @staticmethod
    def hello():
        print("You just called a static method")
        """
        Static method
        Does not use object data or class data

        It behaves like a normal function,
        but is kept inside the class for organization.
        """


lion = Animal('Lion', 22)

# Calling an instance method (needs an object)
lion.speak()

# Calling a class method (works with class data)
lion.clsmethod()

# Calling a static method (independent of object and class data)
lion.hello()