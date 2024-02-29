firstL = input("1st letter: ")
secondL = input("2nd letter: ")
thirdL = input("3rd letter: ")

if (firstL.lower() <= secondL.lower() <= thirdL.lower()) or (thirdL.lower() <= secondL.lower() <= firstL.lower()):
    print(f"The letter in the middle is {secondL}")
elif (secondL.lower() <= firstL.lower() <= thirdL.lower()) or (thirdL.lower() <= firstL.lower() <= secondL.lower()):
    print(f"The letter in the middle is {firstL}")
else:
    print(f"The letter in the middle is {thirdL}")