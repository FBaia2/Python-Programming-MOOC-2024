# Write your solution here
def length_of_longest(my_list:list):
    best = my_list[0]
    for item in my_list:
        if len(item) > len(best):
            best = item
    return len(best)
            









if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)

    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)

