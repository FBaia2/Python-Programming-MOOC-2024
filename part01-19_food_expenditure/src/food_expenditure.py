# Write your solution here
foodFrequency = float(input("How many times a week do you eat at the student cafeteria?"))
dayPrice = float(input("The price of a typical student lunch?"))
weekPrice = float(input("How much money do you spend on groceries in a week?"))

daily = (weekPrice/7) + (dayPrice*foodFrequency/7)
print(f"Daily: {daily} euros")

weekly = (weekPrice) + (dayPrice*foodFrequency)
print(f"Weekly: {weekly} euros")