# Write your solution here
num = int(input("Please type in a positive integer: "))
negVerg = num * -1
for i in range(negVerg, num+1):
    if i != 0:
        print(i)