# The del statement

a = [1, 44.23, 444, 333, 1234.5, 55, 2351]

del a[0] # Delete First element

print(a)

del a[2:4] # Delete elements 2 to 4

print(a)

del a[:] # Delete all the elements

print (a)

del a # Delete the entire object

print (a) # Will give an error
