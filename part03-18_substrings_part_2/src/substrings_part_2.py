# Write your solution here
# Write your solution here
name = input("Please type in a string: ")
x = len(name)
y = x
while y > -1:
    print(name[y:x+1])
    y-=1