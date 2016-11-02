number = 0
total = 0
average = 0.0
count = 0

# loop until something triggered to stop
while True:
    print("Enter a number: ")
    number = float(raw_input())
    if number == -1:
        # stop and exit from the loop
        break
    total = total + number
    count = count + 1
average = total / count
print("Average: " + str(average))
