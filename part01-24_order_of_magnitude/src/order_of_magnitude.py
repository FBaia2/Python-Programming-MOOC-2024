# Write your solution here

numba = int(input("Please type in a number:"))
thankYou = "Thank you!"

if numba > 1000:
    print(thankYou)
elif numba < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print(thankYou)
elif numba < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print(thankYou)
elif numba < 1000:
    print("This number is smaller than 1000")
    print(thankYou)
