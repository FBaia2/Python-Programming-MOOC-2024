# Copy here code of line function from previous exercise
def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])


def square(size, i):
    attempt = 0
    while size != attempt:
        line(size, i)
        attempt +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "o")
