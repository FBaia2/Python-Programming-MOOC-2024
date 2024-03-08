from datetime import date, datetime, timedelta  # Import timedelta

filename = input("Filename: ")
dates = []
times = []
loners = []
liners = []
counter = 0
counting = 0
with open(filename, "w") as my_file:
    starting_date = input("Starting date: ")
    days = int(input("How many days: "))
    print("Please type in screen time in minutes on each day (TV computer mobile):")
    starting_date = starting_date.split(".")
    deez = date(int(starting_date[2]), int(starting_date[1]), int(starting_date[0]))
    for _ in range(days):
        deez1 = datetime.strftime(deez, "%d.%m.%Y")
        screen = input(f"Screen time {deez1}: ")
        dates.append(deez1)
        times.append(screen)
        deez = deez + timedelta(days=1)
     
    for line in times:
        line = line.split(" ")
        liners.append(line)
    
    for i in liners:
        for numba in i:
            numba = int(numba)
            counting += numba

    average = float(counting) / float(days)


    my_file.write(f"Time period: {dates[0]}-{dates[-1]}\n")
    my_file.write(f"Total minutes: {counting}\n")
    my_file.write(f"Average minutes: {average}\n")
    for line in times:
        line = line.replace(" ", "/")
        loners.append(line)
    for _ in range(days):
        my_file.write(f"{dates[counter]}: {loners[counter]}\n")
        counter +=1

    print("Data stored in file late_june.txt")
