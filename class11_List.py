# Heterogeneous Data Structure: can store anything
a = [1, 2.2, 'achyut', 15j, True, print()]
print(a,"\n")

# for exploring list methods use 'help(list)'
#help(list)
# List is mutable & contains duplicates
a[2] = "zeref"

# List can use indexing & slicing

# Deep and Shallow copy!!!

# 1. Reference copy
b = [10,20,30,40]
c = b   # c is reference of b, both point same list in memory
c[-1] = 50
print(f"Actual: {b}, Reference: {c}\n")

# 2. Shallow copy
d = [100,200,300,400]
e = d.copy() # creates new list but changes in e can affect d
e[0] = 999
print(f"Actual: {d},Shallow copy: {e}\n")

# 3. Deep copy
import copy
f = [11,22,33,55,88,99]
g = copy.deepcopy(f) # completely independent copy, does not affect f
g[0] = 7777
print(f"Actual: {f}, Deep copy: {g}\n")

# example showing differnces
mat = [[10,20],[30,40]]

sc = mat.copy()
dc = copy.deepcopy(mat)

sc[0][0] = 999
dc[1][0] = 777

print("Original: ", mat) # [[999, 20], [30, 40]]
print("Shallow copy: ", sc) # [[999, 20], [30, 40]]
print("Deep copy: ", dc) # [[10, 20], [777, 40]]

# shallow copy affects original list meanwhile deep copy doesn't