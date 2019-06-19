# Classes and Objects

class Dog:
    kind = 'Canine'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')

e = Dog('Tuffey')

print(d.kind)

print(e.kind)

print(d.name)

print(e.name)

