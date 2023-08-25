"""
    * How to avoid nested loops using built-in Product() function
"""
from itertools import product

list_a = [1, 2020, 70]
list_b = [2, 4, 7, 2000]
list_c = [3, 70, 7]

#  example
# for a in list_a:
#     for b in list_b:
#         for c in list_c:
#             if a + b + c == 2077:
#                 print(a, b, c)
# 70 2000 7

#  Use product() instead
for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 2077:
        print(a, b, c)

#  Aliasing
a = [1, 2, 3, 5, 6]
b = a
b[4] = 7
print(a)

print(id(a))
print(id(b))

c = [1, 2, 3, 5, 6]
d = c.copy()
d[4] = 7
print(c)
print(d)

print(id(c))
print(id(d))
