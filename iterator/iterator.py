# general for loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print number

# list iterator
it = iter(numbers)
print(next(it))
print(next(it))

# file iterator
fileIt = open('grades.txt', 'r')
print(next(fileIt))

# dictionary iterator
phonebook = {
    'angga': '434636',
    'ari': '363473',
    'wijaya': '5474846'
}

it = iter(phonebook)
print(next(it))
for key in phonebook:
    print(key, phonebook[key])

# work with tupple
square = ((10, 8), (10, 23), (25, 23), (25, 8))
for points in square:
    print(points)
squareit = iter(square)
print(next(squareit))
print(next(squareit))
print(next(squareit))
print(next(squareit))

import os
files = os.popen('ls */*.py')
fileit = iter(files)
while(next(fileit)):
    print next(fileit)
