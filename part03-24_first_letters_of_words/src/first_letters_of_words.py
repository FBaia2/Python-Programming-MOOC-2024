input_string = input("Please type in a string: ")
i = 0
print(input_string[i])  # print the first character of the first word
while i < len(input_string) - 1:
    if input_string[i] == ' ':
        print(input_string[i+1])  # print the first character of the next word
    i += 1
