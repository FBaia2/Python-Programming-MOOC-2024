# Write your solution here
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = input("Operation:")


if operation.lower() == "add":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation.lower() == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation.lower() == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")

