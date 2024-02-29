# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, x, y):
    if x <= len(word) -1 and y <= len(word) -1:
        if word[x] == word[y]:
            return True
        else:
            return False
    else:
        return False








if __name__ == "__main__":
    print(same_chars("abc", 0, 3))