# function is object
def square(number):
    return number * number

sqnum = square(34)
sqnumber = square
sqnum = sqnumber(57)
print("num " + str(sqnum))

numbers = [1, 2, 3, 4]
numbersq = list(map(square, numbers))
print numbersq
