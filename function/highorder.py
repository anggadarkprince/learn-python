def square(number):
    return number * number

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
numbersq = list(map(square, numbers))
print(numbersq)

# filter
def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(numbers)
evens = list(filter(even, numbers))
print(evens)

# reduce
def sum(x, y):
    return x + y

import functools
numbers = list(range(1, 11))
sum = functools.reduce(sum, numbers)
print("The sum is of the range is " + str(sum))
