x = 3
y = 7
z = 10


if x < y and x < z:
    print('something here was the case')
if x < z:
    print(x, 'is less than', z)
elif y < z:
    print(y, 'ls less than than', z)
else:
    print('nothing was the case')

'''
    We can use 'and' and 'or' conditionals for comparison
    x > y and x > z =>
    x > y or y > z =>
'''