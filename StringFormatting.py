#String formatting

#Using formatted String Literals

year = 2019
event = 'referendum'

print(f'Results of the {year} {event}')


# Using str.format()

yes = 43_572_654
no = 43_132_495
per = yes / (yes + no)

# the digit after ':' is the padding
# digit after '.' is number of decimal places

print('{:-9} YES votes {:0.5%}'.format(yes, per))

# using str() and repr()
s = 'Hello,World!'

print(str(s))

print(repr(s))

print(str(1/7))

print(repr(1/7))

x = 10 * 3.25
y = 200 * 200

s = 'The value of x = ' + repr(x) + ', and y is '+ repr(y)

print(s)

hello = 'hello, world \n'

hellorep = repr(hello)

print(hellorep)

print(str(hello))

print(repr((x, y, ('spam', 'eggs'))))

# Formatted string literals (f-strings)

import math

print(f'The value of pi is {math.pi:.4f}')

table = {'Ross': 4127, 'Chandler': 3434, 'Joey':4200}

for name, phone in table.items():
    print(f'{name:14} ===> {phone:10d}')

#Other Modifiers

animals = 'eels'
print(f'My hovercraft is full of {animals}')

print(f'My hovercraft is full of {animals!r}') #!r - repr()

print(f'My hovercraft is full of {animals!a}') #!a - ascii

print(f'My hovercraft is full of {animals!s}') #!s - str()

#String format() method

#positional
print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

#keyword arguments
print('This {food} is {adjective}'.format(food = 'eggs', adjective = 'best'))


# produce a tidily-aligned set of columns

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))




