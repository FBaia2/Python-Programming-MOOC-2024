import string

def separate_characters(my_string: str):
    this1 = ""
    this2 = ""
    this3 = ""

    thisis1 = string.ascii_letters
    thisis2 = string.punctuation

    for letter in my_string:
        if letter in thisis1:
            this1 += letter
        elif letter in thisis2:
            this2 += letter
        else:
            this3 += letter

    return this1, this2, this3

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])  # Letters
    print(parts[1])  # Punctuation
    print(parts[2])  # Other characters
