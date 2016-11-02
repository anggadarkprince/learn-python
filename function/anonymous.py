# anonymous function
# lambda form
def square(number):
    return number * number

sq = lambda x: x*x
print(sq(2))

numbers = [1, 2, 3, 4]
numbersq = list(map(lambda x:x*x, numbers))
print(numbersq)
