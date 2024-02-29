# Write your solution here
# Write your solution here
gemmeString = input("Please type in a string:")
x = int(len(gemmeString))
lep = int(((30 - x)/2)-1) * " "
if x % 2 == 1:
    print(30 * "*")
    print("*" + lep + gemmeString + lep +" " + "*")
    print(30 * "*")
else:
    print(30 * "*")
    print("*" + lep + gemmeString + lep + "*")
    print(30 * "*")