# Write your solution here
def longest(strings: list):
    best = strings[0]
    for i in strings:
        if len(i) > len(best):
            best = i
    return best






if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))