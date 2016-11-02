numer = 0
denom = 0
while denom != -1:
    print("Enter a numerator: ")
    numer = float(raw_input())
    print("Enter a denomenator: ")
    denom = float(raw_input())
    if denom == 0:
        # continue next iteration instead process code below
        continue
    print(numer / denom)
