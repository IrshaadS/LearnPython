# Iterators and Generators 


#Iterator

class Reverse:
    """ Iterator for looping over a sequence backwards """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1

        return self.data[self.index]
    
rev = Reverse('idea')

iter(rev)

for char in rev:
    print(char)

print(rev)


#Generator

def rever(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in rever('data'):
    print(char)



# Generator examples

print(sum(i*i for i in range(10)))

vectorX = [10, 20, 30]

vectorY = [7, 5, 3]

print(sum(x*y for x, y in zip(vectorX, vectorY)))


from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

print(sine_table)

unique_words = set(word  for line in page  for word in line.split())

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))

