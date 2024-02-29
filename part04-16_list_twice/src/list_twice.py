original = []
inp = 1
while True:
    inp = int(input("New item: "))
    if inp == 0:
        break
    else:
        original.append(inp)
        in_order = sorted(original)
        print(f"The list now: {original}")
        print(f"The list in order: {in_order}")

print("Bye!")