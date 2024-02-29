def distinct_numbers(my_list):
    my_list.sort()
    new_list = [my_list[0]]
    for i in range(1, len(my_list)):
        if my_list[i] != my_list[i-1]:
            new_list.append(my_list[i])
    return new_list

if __name__ == "__main__":
    print(distinct_numbers(my_list = [3, 2, 2, 1, 3, 3, 1]))
