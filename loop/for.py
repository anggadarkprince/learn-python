# simple for loop
for i in [1, 2, 3, 4, 5]:
    print i

# more for loop example
numbers = [1, 2, 3, 4, 5, 6 ,7 ,8, 9, 10]
sum = 0
for i in numbers:
    print i * 3
    sum = sum + i
print "Sum result: " + str(sum)

# loop characters
word = "hello"
for char in word:
    print char

# another character loop
sentence = "now is the time for all good people to came to the aid"
count = 0
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or  letter == 'o' or \
    letter == 'u':
        count = count + 1
print 'The number of vowels is ' + str(count)

# loop through index 0 - 9
for i in range(0, len(numbers)):
    print numbers[i];

 # jump 3 numbers
for i in range(0, len(numbers), 3):
    print numbers[i];

# work with tupple
words = ('now', 'is', 'the', 'time')
for word in words:
    print word

# work with dictionary
phonebook = {
    'angga': '434636',
    'ari': '363473',
    'wijaya': '5474846'
}
print str(phonebook['angga'])
print(phonebook.keys())
print(phonebook.values())
for key in phonebook.keys():
    print(key + "'s phone is: " + phonebook[key])
