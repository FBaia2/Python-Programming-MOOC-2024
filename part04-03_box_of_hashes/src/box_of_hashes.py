# Copy here code of line function from previous exercise
def line(num, x):
    if x == "":
        print(num * "*")
    else:
        print(num * x[0])

if __name__ == "__main__":
    line(5, "x")

def box_of_hashes(height):
    # You should call function line here with proper parameters
    attempt = 0
    while height != attempt:
        line(10, "#")
        attempt += 1 

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
