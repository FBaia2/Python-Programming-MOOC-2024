# Write your solution here
# You can test your function by calling it within the following block

def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])

if __name__ == "__main__":
    line(5, "x")
