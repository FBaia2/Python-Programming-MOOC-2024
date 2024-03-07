from datetime import datetime, timedelta
day = input("Day: ")
month = input("Month: ")
year = input("Year: ")
eve = datetime(1999, 12, 31)
user = datetime(int(year),int(month), int(day))
difference = eve - user
if difference.days <= 0:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {difference.days} days old on the eve of the new millennium.") 


