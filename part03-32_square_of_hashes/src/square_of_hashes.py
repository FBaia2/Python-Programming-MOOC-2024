# Write your solution here
# You can test your function by calling it within the following block

def hash_square(length):
    attempts = 0
    while attempts < length:
        print("#"* length)
        attempts += 1


if __name__ == "__main__":
    hash_square(5)