s = {10, 20, 30}

"""
SET NOTES (Python)

- {} creates a dictionary, use set() for empty set
- Set stores only hashable (immutable) elements
- tuple is hashable, list is not
- No duplicate values
- Unordered collection
- No indexing or slicing
- Set is mutable, but elements must be immutable
- Set operations are method/operator driven
"""

# Traversing a set
set_ = {12, 14, 15}
for i in set_:
    print(i)

print()

# Basic operations
x = {10, 20, 30}
x.add(40)

# Copy
y = x.copy()  # shallow copy

y = {30, 40, 50, 60}

print("Difference (y - x):", y.difference(x))  # elements in y not in x
print("Intersection:", x & y)                  # common elements
print("Symmetric Difference:", x ^ y)          # uncommon elements
print("Union:", x | y)                          # all unique elements
print()

x.discard(40)  # remove without error if missing
print(x)
print()

# Subset & Superset
a = {10, 20, 30, 40, 50, 60}
b = {10, 20, 30}

print("b is subset of a:", b.issubset(a))       # or b <= a     b == a (for equality)
print("a is superset of b:", a.issuperset(b))   # or a >= b
