def double_items(numbers: list) -> list:
    num = []
    for item in numbers:
        num.append(item * 2)
    return num

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    print(double_items(numbers))
