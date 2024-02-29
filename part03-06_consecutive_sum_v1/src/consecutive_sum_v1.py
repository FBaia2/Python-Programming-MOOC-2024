limit = int(input("Limit: "))  # Asks the user to input a limit and converts it to an integer
sum = 0  # Initializes the sum of consecutive numbers
i = 1  # Initializes the first number to be added to the sum
verdict = ""
while sum < limit:  # Continues to add numbers to the sum until it is at least equal to the limit
    sum += i  # Adds the current number to the sum
    i += 1  # Increments the number to be added
    verdict += str(i)
    verdict += "+"
print(f"{verdict} = {sum}")
  # Prints the final sum
