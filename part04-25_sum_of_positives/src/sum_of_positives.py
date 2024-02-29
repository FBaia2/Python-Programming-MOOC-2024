# Write your solution here
def sum_of_positives(my_list: list):
    sum = 0
    for i in my_list:
        if i > 0:
            sum += i
    print(f"The result is {sum}")
    return sum


if __name__ == "__main__":
    sum_of_positives(my_list = [1, -2, 3, -4, 5])
