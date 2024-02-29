phone_book = {}
command = 0
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    
    if command == 2:  # Add
        name = input("name: ")
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    
    
    
    elif command == 1:  # Search
        name = input("name: ")
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")
            
    
        
    elif command == 3:  # Quit
        print("quitting...")
        break
