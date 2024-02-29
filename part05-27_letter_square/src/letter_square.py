num = int(input("Layers: "))

letters = {i: chr(65 + i) for i in range(26)}

for i in range(num * 2 - 1):
    for j in range(num * 2 - 1):
        dist = max(abs(num - 1 - i), abs(num - 1 - j))
        print(letters[dist], end="")
    print()

  
    






