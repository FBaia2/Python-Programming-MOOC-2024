# Write your solution here
name = input("Please type in a string: ")
numbaMax = len(name)
second = name[1]
last = name[numbaMax-2]

if second.lower() == last.lower():
    print(f"The second and the second to last characters are {name[1]}")
else:
    print("The second and the second to last characters are different")