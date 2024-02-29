# Write your solution here
hourlyWage = float(input("Hourly wage: "))
hoursWorked = float(input("Hours worked: "))
dayWeek = (input("Day of the week: "))

if dayWeek.lower() == "sunday":
    print(f"Daily wages: {(hoursWorked * hourlyWage)*2} euros")
else:
    print(f"Daily wages: {(hoursWorked * hourlyWage)} euros")