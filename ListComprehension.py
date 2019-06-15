
#List comprehensions

squares = [x**2 for x in range(10)]

print(squares)

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])


#Create a list with values doubled

vec = [-4, -2, 0, 2,4]

print([x*2 for x in vec])


#Filter the -ve numbers from list

print([x for x in vec if x >= 0])

# Call a method on each element of array

freshfruit = ['banana', 'loganberry', 'passion fruit']

print([(x, len(x)) for x in freshfruit])

# List of number and its square

print([(x, x**2) for x in range(1, 10)])

#Flattening multiple lists into one list

vec = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

print([num for elem in vec for num in elem])

