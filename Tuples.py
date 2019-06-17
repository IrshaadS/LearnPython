t = 12234, 43212, 'hello!'

print(t[0])


#Nested tuple

u = t, (1, 123, 'hello!')

print(u)

# Immutable
# t[0] = 45

# print(t) # gives an error

#objects inside the tuple are mutable

v = ([123,3,3])
print(v)



#Empty tuple

empty = ()

print(len(empty))

singleton = 'hElLo!', #additional comma

print(len(singleton))

x, y, z = t #unpacking

print(x)
print(y)
print(z)

p, q, r = 1, 2, 4

print(p, q, r)
