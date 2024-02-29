# Write your solution here
# You can test your function by calling it within the following block

def spruce(num):
    i = 0
    space = num
    l = 1
    print("a spruce!")
    while i != num:
        space -=1
        print(space * " ", end="")
        print(l * "*")
        l += 2
        i += 1
        if i == num:
            print((num -1) * " ", end="")
            print(1 * "*")
    
    

        


 

if __name__ == "__main__":
    spruce(5)