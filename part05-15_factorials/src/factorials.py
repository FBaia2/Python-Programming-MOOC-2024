def factorials(n: int):
    results = {1: 1}
    for i in range(2, n+1):
        results[i] = results[i-1] * i
    return results

if __name__ == "__main__":
    k = factorials(5)
    print(k[5])
