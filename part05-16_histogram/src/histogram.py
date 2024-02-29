def histogram(s):
    letters = list(s)
    words = {}
    for word in letters:
        # if the word is not yet in the dictionary, initialize the value to zero
        if word not in words:
            words[word] = 0
        # increment the value
        words[word] += 1
    for key, value in words.items():
        print(key, value * "*")

# call the function
if __name__ == "__main__":
    
    histogram("soapbar")

