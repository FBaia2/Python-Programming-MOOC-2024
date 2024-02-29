def no_vowels(word):
    new_word = word
    for i in "aeiou":
        new_word = new_word.replace(i, "")
    return new_word

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))
