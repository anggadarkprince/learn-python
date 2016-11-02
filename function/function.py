# common function
def square(number):
    print number * number

def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if  string[i] == 'a' or string[i] == 'e' or \
            string[i] == 'i' or string[i] == 'o' or \
            string[i] == 'u':
            count += 1
    print(count)

# return function
def ftoc(temp):
    return (temp - 32.0) * (5.0 / 9.0)

square(2)
numVowels('angga')
print(ftoc(52))
