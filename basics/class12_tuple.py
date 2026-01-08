# tuple can store different data types
# that is heterogenous nature
tup = (12, 1.2, 12j, "z")

#help(tuple)   # not much methods to use
 
# tuple is immutable (cannot change values)
# tup[0] = 100  # TypeError

# tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c,"\n")

# tuple creation edge cases
p = ()        # empty tuple
q = (55)      # int (not a tuple)
r = (55,)     # single-element tuple

# indexing and slicing
nums = (10, 20, 30, 40, 50)
print(nums[0])
print(nums[1:4],"\n")

# list to tuple
lst = [10, 20, 30, 41, 50, 60, 70, 80]
tuple_ = tuple(lst)
print(tuple_)