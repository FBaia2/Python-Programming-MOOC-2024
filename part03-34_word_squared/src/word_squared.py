def squared(text, x):
    length = len(text)
    longth = length * x
    product = text * longth
    prodLen = len(product)
    i = x
    vari = 0
    attempt = 0
    while attempt < i:
        attempt += 1
        print(product[vari:x])
        vari += i
        x += i

if __name__ == "__main__":
    squared("qwerty", 37)
