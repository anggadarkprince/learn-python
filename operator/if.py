# simple if
print("Enter hours worked: ")
hoursWorked = int(raw_input())
rate = 25.00

if hoursWorked > 40:
    grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
if hoursWorked <= 40:
    grossPay = hoursWorked * rate
print("Gross Pay: " + str(grossPay))
