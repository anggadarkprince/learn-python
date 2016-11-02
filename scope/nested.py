import math

def hypotenuse(s1, s2):
    def square(num):
        return num * num
    return math.sqrt(square(s1) + square(s2))

print(hypotenuse(3, 5))
