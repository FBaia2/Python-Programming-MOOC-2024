attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1


   
    if code == "4321" and attempts == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif code == "4321" and attempts > 1:
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")