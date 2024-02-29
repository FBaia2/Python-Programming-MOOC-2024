def everything_reversed(x):
    y = x[::-1]
    for i in range(len(y)):
        y[i] = y[i][::-1]
    return y


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)