# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block

def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])


def shape(a, b, c, d):
   
    i = 1
    while i <= a:
        line(i, b)
        i += 1

    i = 1
    while i <= c:
        line(a, d)
        i += 1





if __name__ == "__main__":
    shape(5, "x", 2, "o")