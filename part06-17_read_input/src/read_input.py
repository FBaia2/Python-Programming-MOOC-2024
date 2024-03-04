def read_input(cmd: str, x : int, y: int):
    while True:
        num = input(cmd)
        if  num.isdigit():
            if num >= x and num <= y:
                return num
            else:
                print(f"You must type in an integer between {x} and {y}")
        else:
            print(f"You must type in an integer between {x} and {y}")
        















if __name__== "__main__":
    number = read_input("Please type in a number: ", 5, 10)
print("You typed in:", number)
