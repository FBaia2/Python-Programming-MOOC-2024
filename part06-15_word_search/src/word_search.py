def find_words(search_term: str):
    results = []
    counter = 0
    with open("words.txt") as my_file:
        for line in my_file:
            word = line.strip()
            if "*" in search_term:
                if search_term[0] == "*":
                    if word.endswith(search_term[1:]):
                        results.append(word)
                elif search_term[-1] == "*":
                    if word.startswith(search_term[:-1]):
                        results.append(word)
            elif "." in search_term:
                if len(word) != len(search_term):
                    continue
                else:
                    match = True
                for i in range(len(word)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                if match:
                    results.append(word)
            else:
                if word == search_term:
                    results.append(word)
    return results



if __name__=="__main__":
    print(find_words("*a"))
