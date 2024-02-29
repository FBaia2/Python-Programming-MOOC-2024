# Write your solution here
def most_common_character(word):
    best = word[0]
    for item in word:
        if word.count(item) > word.count(best):
            best = item

    return best
        


     




if __name__ == "__main__":

    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
