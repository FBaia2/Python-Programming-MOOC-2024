word = []
while True:
    inputing = input("Word: ")
    if inputing not in word:
        word.append(inputing)
    else:
        break

print(f"You typed in {len(word)} different words")
