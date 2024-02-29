from math import sqrt
# Write your solution here

while True:
    code = float(input("Please type in a number: "))
    if code == 0:
        break
    elif code > 0:
        print(sqrt(code))
    elif code < 0:
        print("Invalid number")

print("Exiting...")