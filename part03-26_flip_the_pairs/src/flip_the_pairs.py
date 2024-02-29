num = int(input("Please type in a number: "))
i = 1
while i <= num:
    if i % 2 == 0:  # if i is even
        print(i)
        print(i - 1)
    elif i == num:  # if i is the last number and it's odd
        print(i)
    i += 1
