"""
    Dunder / Magic Methods:
    - Special Python methods that start and end with "__"
    - They let your class behave like built-in types (int, list, str, etc.)

    Common ones:
    __init__()      -> runs when object is created
    __str__()       -> runs when you print(object)
    __len__()       -> runs when you do len(object)
    __add__()       -> runs when you do object1 + object2
"""


# __str__()
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        # This decides what should be printed when we do print(obj)
        # Without __str__, Python prints something like: <Students object at 0x...>
        return f"name: {self.name} & marks: {self.marks}"


obj = Students("Zeref", 99.99)
print(obj)  # print(obj) automatically calls obj.__str__()


# __len__()
class Shopping:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        # len(obj2) calls obj2.__len__()
        # Here we return the length of the items list inside the object
        return len(self.items)
    

obj2 = Shopping(['apple', 'banana', 'milk', 'bread'])
print(len(obj2))

# NOTE:
# Without __len__(), len(obj2) gives error because Python doesn't know
# what "length" means for your custom class


# __add__()
class Numbers:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, custom):
        # a + b calls a.__add__(b)
        # custom is the second object (b)
        return self.num + custom.num


a = Numbers(15)
b = Numbers(35)
print(a + b)

# NOTE:
# Without __add__(), a + b gives error because Python can't add two objects directly
# With __add__(), we teach Python: "add their .num values"