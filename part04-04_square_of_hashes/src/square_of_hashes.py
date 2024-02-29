# Copy here code of line function from previous exercise
def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])


def square_of_hashes(size):
    attempt = 0
    while size != attempt:
        line(size, "#")
        attempt +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
