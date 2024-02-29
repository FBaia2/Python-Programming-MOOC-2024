# limit = int(input("Limit: "))  # Asks the user to input a limit and converts it to an integer
# sum = 1  # Initializes the sum of consecutive numbers
# i = 0  # Initializes the first number to be added to the sum
# verdict = ""
# while sum < limit:  # Continues to add numbers to the sum until it is at least equal to the limit
#     sum += i  # Adds the current number to the sum
#     i += 1  # Increments the number to be added
#     verdict += str(i)
#     verdict += "+"
# print(f"{verdict} = {sum}")
#   # Prints the final sum

limit = int(input("Limit: "))  # Asks the user to input a limit and converts it to an integer
sum = 0  # Initializes the sum of consecutive numbers
i = 1  # Initializes the first number to be added to the sum
verdict = ""
while sum < limit:  # Continues to add numbers to the sum until it is at least equal to the limit
    sum += i  # Adds the current number to the sum
    if i != 1:  # Avoids adding "+" before the first number
        verdict += " + "
    verdict += str(i)
    i += 1  # Increments the number to be added
print(f"The consecutive sum: {verdict} = {sum}")  # Prints the final sum
