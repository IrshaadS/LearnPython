# Dictionary 

tel = {'jack': 4098, 'sape': 4139}
tel['guide'] = 4127

print(tel)

print(tel['jack'])

del tel['sape']

tel['irv'] = 4127

print(tel)

print(list(tel)) # lists keys used 

print(sorted(tel))

print('guide' in tel)

print('jack' not in tel)


# Dictionary constructor

dc = dict([('sape', 1234),('guido',5656)])

print(dc)

# dict comprehensions

dcomp = {x:x+1 for x in (2, 4, 5, 6, 7, 8) if(x %2) == 0}

print(dcomp)

#Looping Techniques
knights = {'gallahad': 'the pure', 'robin':'the brave'}

for k, v in knights.items():
    print(k, v)

#Looping over 2 or more sequences
questions = ['name', 'quest', 'favourite colour']
answers = ['lanceleot', 'the holy grail', 'blue']


for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}'.format(q, a))

# Looping over reverse sequence
for i in reversed(range(1, 10)):
    print(i)

# Looping over a sequence in sorted order

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    print(f)

#
# It is sometimes tempting to change a list while you are looping over it; 
# however, it is often simpler and safer to create a new list instead.

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)





