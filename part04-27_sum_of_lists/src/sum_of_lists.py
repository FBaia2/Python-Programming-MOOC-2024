def list_sum(a:list, b:list):
    c = [0]
    i = 0
    while True:
        d = a[i] + b[i]
        c.append(d)
        i += 1
        if len(c) > len(a):
            c.remove(0)
            return c




if __name__ == "__main__":
    print(list_sum(a = [1, 2, 3], b = [7, 8, 9]))