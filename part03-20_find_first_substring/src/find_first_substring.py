# Write your solution here
attempts = 0
word = input("Please type in a word: ")
carac = input("Please type in a character: ")
lenght = len(word)+1
i = word.find(carac)
if lenght - i > 3:
    print(word[i:i+3])