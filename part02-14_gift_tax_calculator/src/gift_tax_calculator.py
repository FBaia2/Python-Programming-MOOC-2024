
giftValue = int(input("Value of gift: "))

eight = (100 + (giftValue - 5000) * 0.08)
ten = (1700 + (giftValue - 25000) * 0.1)
twelve = (4700 + (giftValue - 55000) * 0.12)
fifteen = (22100 + (giftValue - 200000) * 0.15)
seventeen = (142100 + (giftValue - 1000000) * 0.17)

if giftValue > 1000000:
    print(f"Amount of tax: {seventeen}")
elif giftValue < 1000000 and giftValue > 200000:
    print(f"Amount of tax: {fifteen}")
elif giftValue < 200000 and giftValue > 55000:
    print(f"Amount of tax: {twelve}")
elif giftValue < 55000 and giftValue > 25000:
    print(f"Amount of tax: {ten}")
elif giftValue < 25000 and giftValue > 5000:
    print(f"Amount of tax: {eight}")
else:
    print("No tax!")
    