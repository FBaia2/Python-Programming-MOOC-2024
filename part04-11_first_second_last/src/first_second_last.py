def first_word(sentence):
    num = sentence.find(" ")
    return sentence[0:num]
    

def second_word(sentence):
    num = sentence.find(" ")
    sentence2 = sentence[num+1:]
    num2 = sentence2.find(" ")
    if num2 == -1:  # If there's no second space, return the whole remaining string.
        return sentence2
    else:
        return sentence2[0:num2]

    

def last_word(sentence):
   num3 = sentence.rfind(" ")
   return sentence[num3+1:]

# The if statement is aligned with the def statements, so Python knows it's not part of any function.
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))