# while loop
# A while loop runs as long as the condition is True.
# It is useful when the number of iterations is NOT known.

# Example 1: countdown using while loop
i = 5
while i > 0:
    print(i)
    i -= 1  # update the variable to avoid infinite loop

print()

# Example 2: printing characters of a string using index
name = "Achyut"
index = 0
while index < len(name):
    print(name[index])
    index += 1

print()

# Example 3: using while loop with break
i = 0
while True:
    if i == 3:
        break  # exits the loop
    print(i)
    i += 1
