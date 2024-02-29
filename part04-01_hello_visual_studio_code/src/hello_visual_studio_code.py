# Write your solution here

while True:
    text = input("Editor:")
    if text.lower() == "word" or text.lower() == "notepad":
        print("awful")
    elif text.lower() == "emacs" or text.lower() == "vim":
        print("not good")
    elif text.lower() == "visual studio code":
        print("an excellent choice!")
        break

