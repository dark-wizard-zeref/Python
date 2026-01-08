age = int(input("Enter age: "))

# indentation (4 spaces) is important
if age >= 18:
    print("vote")
else:
    print("grow up")

# ternary operator
print("vote") if age >= 18 else print("grow up")

# elif example
rs = int(input("Enter 0 / 10 / 20 / 30: "))

if rs == 10:
    print("chips")
elif rs == 20:
    print("ice-cream")
elif rs == 30:
    print("cone")
else:
    print("no money")