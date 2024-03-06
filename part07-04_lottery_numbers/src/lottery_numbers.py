from random import randint

def lottery_numbers(amount: int, lower: int, upper: int):

    lottery_nums = []
    while len(lottery_nums) < amount:
        new_rnd = randint(lower, upper)
        if new_rnd not in lottery_nums:
           lottery_nums.append(new_rnd)

    lottery_nums.sort()

    return lottery_nums

if __name__=="__main__":
    for number in lottery_numbers(3, 2, 22):
        print(number)
