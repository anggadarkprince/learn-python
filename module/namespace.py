import newton

def square(number):
    print("Not from the newton module")
    return number * number

print("Square from newton.py:")
print(newton.square(9))
print("Square from main program")
print(square(4))
