# Copy here code of line function from previous exercise
def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])


def triangle(num):
    i = 1
    while i <= num:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(5)