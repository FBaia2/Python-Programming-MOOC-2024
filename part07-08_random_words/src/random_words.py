import random
def words(n: int, beginning: str):
    palabra = []
    palabra_braba = []
    with open("words.txt") as my_file:
        
        for line in my_file:
            line = line.replace("\n", "")
            if line.startswith(beginning):
                palabra.append(line)

        if len(palabra) >= n:
            while len(palabra_braba) < n:
                new_pal = random.choice(palabra)
                if new_pal not in palabra_braba:
                    palabra_braba.append(new_pal)
        else:
            raise ValueError ("There are not enough words in the file")
    
    return palabra_braba




if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)