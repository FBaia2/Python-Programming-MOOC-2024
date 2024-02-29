word = input("Please type in a word: ")
char = input("Please type in a character: ")

# Start from the first occurrence of the specified character
start = word.find(char)

while start != -1 and start <= len(word) - 3:
    # Print the substring starting from the current character that is exactly four characters long
    print(word[start:start+3])
    
    # Move to the next occurrence of the specified character
    start = word.find(char, start + 1)
