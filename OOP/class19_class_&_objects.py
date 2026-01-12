class Factory:
    a = 13  # class attribute, shared by all objects

    def hello(self):  # instance method, self refers to calling object
        print("Hi, how are you")


# class is created once when program runs
# objects can be created multiple times

print(Factory.a)     # accessing class attribute using class

obj = Factory()      # object creation

print(obj.a)         # accessing class attribute using object
obj.hello()          # calling method using object