from datetime import date
filename = input("Filename: ")
with open(filename, "a") as new_file:
    starting_date = input("Starting date: ")
    days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    starting_date = starting_date.split(".")
    print(starting_date)
    deez = date(int(starting_date[0]), int(starting_date[1]), int(starting_date[2]))
    print(deez)
    for _ in range(days):
        screen = input(f"Screen time {starting_date}: ")





    print("Data stored in file late_june.txt")