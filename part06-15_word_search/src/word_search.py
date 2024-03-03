def find_words(search_term: str):
    count_asterisk = 0
    if "." not in search_term or "*" not in search_term:
        with open("words.txt") as my_file:
            for line in my_file:
                # line.replace("\n", "")
                if search_term in line:
                    print(line)
    elif "*" in search_term:
        for i in search_term:
            if "*" in search_term:
                count_asterisk +=1
                if count_asterisk > 1:
                    print("you can't have more then one asterisk")
                else:
                    if search_term[0] == "*":
                    elif search_term[-1] == "*":


    elif "." in search_term:












if __name__ == "__main__": 
    print(find_words("vokes"))