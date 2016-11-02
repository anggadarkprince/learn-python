# simple while
number = 1
while(number <= 10):
    print(number)
    number = number + 1

# another while example
sum = 0
number = 1
while number <= 10:
    sum = sum + number
    number = number + 1
print("The sum is " + str(sum))

# work with while loop
balance = 5000
rate = 1.02
year = 1
while year <= 10:
    balance = balance * rate
    print("Year: " + str(year) + ": " + str(balance))
    year = year + 1
