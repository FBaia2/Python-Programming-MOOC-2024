num = int(input("Please type in a number:"))
while num > 0:
    i = num
    sum = 1
    while i > 1:
        sum *= i
        i -= 1
    print(f"The factorial of the number {num} is {sum}")
    num = int(input("Please type in a number:"))
print("Thanks and bye!")
