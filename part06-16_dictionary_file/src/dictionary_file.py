eng_name = ""
fin_name = ""
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    func = input("Function: ")
    if func == "3":
        print("Bye!")
        break
    elif func == "1":
        fin_name = input("The word in Finnish: ")
        eng_name = input("The word in English: ")
        print("Dictionary entry added")
        with open("dictionary.txt", "a") as my_file:
            my_file.write(f"{fin_name} - {eng_name}\n")
    elif func == "2":
        search_term = input("Search term: ")
        with open("dictionary.txt") as my_file:
            for line in my_file:
                if search_term in line:
                    print(line)
