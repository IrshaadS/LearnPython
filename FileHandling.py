# File handling

f = open('workfile.txt', 'a')
f.write('added through file handling')
f.close()

with open('workfile.txt') as f:
    read_data = f.read()

print(read_data)

print(f.closed)

f = open('workfile.txt')
f.read()

f.close()

f = open('workfile.txt')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())


for line in f:
    print(line, end='')

f = open('newfile.txt', 'rb+')
f.write(b'0123456789abcdef')

print(f.seek(5)) #goto 6th byte
print(f.read(1))
print(f.seek(-3, 2)) # goto 3rd byte from end
print(f.read(1))