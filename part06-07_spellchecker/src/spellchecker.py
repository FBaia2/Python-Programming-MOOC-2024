texting = input("Write text: ")
lista = texting.split()


listama = []



with open("wordlist.txt") as new_file:
    wordlist_content = new_file.read().split()  
    for word in lista:
        if word.lower() not in wordlist_content:
            listama.append(word)
counter = -1
for word in lista:
    counter += 1
    if word in listama:
        lista[counter] = "*" + word + "*" 
        




s = ', '.join(lista)
new_s = s.replace(", ", " ")
print(new_s)

