last_num = 0
count = 0
suma = 0
mean = 0
positives = 0
negatives = 0

print("Please type in integer numbers. Type in 0 to finish.")

while True:

    numa = int(input("Number:"))
    suma = suma + numa
    if numa == 0:
        break
    count += 1
    if numa > 0:
        positives += 1
    elif numa < 0:
        negatives += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {suma}")
print(f"The mean of the numbers is {suma/count}")
print(f"Positive numbers {positives}")
print(f"Negative numbers {negatives}")

