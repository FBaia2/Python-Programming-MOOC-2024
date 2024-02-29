numba = int(input("Please type in a number:"))

if numba < 0:
    print("The absolute value of this number is " + str(numba*-1))
elif numba > 0:
    print(f"The absolute value of this number is {numba}")
else:
    print("The absolute value of this number is 0")