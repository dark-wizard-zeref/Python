"""
    Encapsulation:
    - Keeping variables (data) + functions (methods) together inside a class
    - Python doesn't truly block access like some languages
    it mostly uses naming styles to "suggest" what you should / shouldn't touch

    Access levels in Python:
    1) Public   -> normal name (name)
    2) Protected -> starts with _  (means: "internal use, don't touch outside", have a look at eg below)
    3) Private  -> starts with __ (Python hides/renames it internally)
"""

class Animal:
    name = "Lion"      # Public: anyone can access
    _age = 12          # Protected-style: still accessible, but you SHOULD avoid using it outside
    __gender = "M"     # Private-style: can't access directly using __gender outside the class

    def _info(self):
        # Protected-style method: still callable, but meant for internal use
        # This method can access __gender because it's inside the same class
        print(f"Gender: {self.__gender}")


class Cat(Animal):
    name = "Cat"
    # Cat inherits everything from Animal
    # But it cannot directly use __gender by writing self.__gender
    # because __gender is "private-style" for Animal


neko = Cat()

# Public + protected-style attribute access
print(f"name: {neko.name}, age: {neko._age}")

# This will NOT work:
# print(neko.__gender)  # ERROR: 'Cat' object has no attribute '__gender'

# This works because the method is inside Animal
neko._info()

# Extra (not recommended):
# You can still access private-style variables like this because Python renames them internally:
# print(neko._Animal__gender)