num = int(input("Please type in a number: "))
start = 1
end = num

while start <= end:
    if start != end:
        print(start)
        print(end)
    else:
        print(start)
    start += 1
    end -= 1
