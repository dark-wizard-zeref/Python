# arithmetic operators
"""
+
-
*
/   gives result in float
//  integer division (floor division)
%   gives remainder
**  exponential operator (9**2 -> 9^2)
"""

# python follows BODMAS -> () ** * / + -
a = 10 / 2 * (4 / 2)
print(a)

# assignment operators
"""
shorthand operators:
+=, -=, *=, /=, %=, //=

string uses + for concatenation
string uses * for repetition
"""

a = 12
a += 8
print(a)

name = "Achyut"
last_name = "Shinde"
print(name +" "+ last_name)
print(name * 5)

# comparison operators
"""
>, >=, <, <=, ==, !=
result is boolean
"""

# logical operators
"""
and, or, not
"""

# operator chaining
print(not 12 == 12 == True)  # (12 == 12) and (12 == True)