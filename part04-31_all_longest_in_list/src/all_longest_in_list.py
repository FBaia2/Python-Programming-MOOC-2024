# Write your solution here
# Write your solution here
def all_the_longest(my_list: list):
    best_list= []
    best = my_list[0]
    for item in my_list:
        if len(item) > len(best):
            best = item
    best_list.append(best)        
    for item in my_list:
        if len(item) == len(best) and item != best:
            best_list.append(item)
    return best_list

            


if __name__ == "__main__":

    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)

    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)

