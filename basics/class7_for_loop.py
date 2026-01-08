# for loop with range (start, stop, step)
for i in range(5, 0, -1):
    print(i)

print()

# iterating over a string
for i in "Achyut":
    print(i)

print()

# for-else example
for i in range(4):
    if i < 4:
        print(i)
    else:
        break
else:
    # executes only if loop finishes normally (no break)
    print("loop ends after 11")