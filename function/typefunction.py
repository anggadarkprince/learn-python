# boolean function
def isVowel(letter):
    if  letter == 'a' or letter == 'e' or \
        letter == 'i' or letter == 'o' or \
        letter == 'u':
        return True
    else:
        return False

# predicate function
def numVowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if  isVowel(string[i]):
            count += 1
    print(count)

numVowels('angga ari wijaya')
