#Nested List comprehension

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print([[row[i] for row in matrix] for i in range(4)])


# Without List Comprehension

transposed = []

for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

# Without List Comprehension

transposed2 = []

for i in range(4):
    transposed_row = []
    
    for row in matrix:
        transposed_row.append(row[i])
    
    transposed2.append(transposed_row)

print(transposed2)

# built in function
print(list(zip(*matrix)))


