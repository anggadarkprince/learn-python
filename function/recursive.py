
def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number-1)

print(fact(5))


def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])

print(explode('angga'))


def removeDups(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return removeDups(word[1:])
    else:
        return word[0] + removeDups(word[1:])

print removeDups('aannggaa')
