story = ""
last_word = ""
while True:
    word = input("Please type in a word: ")
    if word.lower() == last_word.lower() or word.lower() == "end":
        break
    last_word = word
    story += word + " "


print(story)
