# Write your solution here

name = input("Please tell me your name:")
if name.lower() == "jerry":
    print("Next please!")
else:
    portionSoup = int(input("How many portions of soup?"))
    if portionSoup > 0:
        totalCost = portionSoup*5.90
    
        print(f"The total cost is {totalCost}")
        print("Next please!")
