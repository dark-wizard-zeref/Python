class Factory:
    def __init__(self, material, zips, pockets):
        """
        This method runs automatically when we create a new object
        from the Factory class.

        'self' refers to the current object being created.
        It helps us store data inside that specific object.
        """

        print(self)     # This prints the memory location of the object
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show_details(self):
        print(
            f"\tmaterial: {self.material},\n"
            f"\tzips: {self.zips},\n"
            f"\tpockets: {self.pockets}\n"
        )


# Python allocates memory for this object
# and 'self' refers to that memory location
reebok = Factory("Leather", 3, 3)
reebok.show_details()

# Creating another object named 'campus'
# This object has a different memory location
campus = Factory("Nylon", 2, 2)
campus.show_details()


