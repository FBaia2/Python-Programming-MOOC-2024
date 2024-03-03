while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    txt = input("Function: ")
    if txt == "0":
        print("Bye now!")
        break
    elif txt == "1":
        with open("diary.txt", "a") as my_file:
            deez = input("Diary entry:")
            my_file.write(deez + "\n")
            # print(deez, file=my_file)
            print("Diary saved")
    elif txt == "2":
        with open("diary.txt") as my_file:
            contents = my_file.read()
            print(contents)
