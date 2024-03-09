import difflib

texting = input("Write text: ")
lista = texting.split()

listama = []

with open("wordlist.txt") as new_file:
    wordlist_content = new_file.read().split()
    for word in lista:
        if word.lower() not in wordlist_content:
            listama.append(word)

for word in lista:
    if word in listama:
        suggestions = difflib.get_close_matches(word, wordlist_content, n=3, cutoff=0.6)
        if suggestions:
            print("suggestions:")
            print(f"*{word}* (Did you mean: {', '.join(suggestions)})")
        else:
            print(f"*{word}* (No close matches found)")
    else:
        print(word, end=" ")

# Print a newline for readability
print("\n")
