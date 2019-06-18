# Sets 

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

print('orange' in basket) # membership testing

print('crabgrass' in basket)

#Set operations

a = set('abracadabra')

b = set('alacazam')

print(a) # unique elements of a

print(a-b) # elements in a but not in b

print(a|b) # a union b

print(a&b) # a intersection b

print(a^b) # elements in a or b but not both

# Set Comprehension

a = {x for x in 'abracadabra' if x not in 'abc'}

print(a)



