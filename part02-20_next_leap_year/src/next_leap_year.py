# Write your solution here
year = int(input("Year:"))
year1 = year
while True:
    year += 1
    if year % 4 == 0 and year % 100 != 0:
        print(f"The next leap year after {year1} is {year}")
        break
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(f"The next leap year after {year1} is {year}")
        break

