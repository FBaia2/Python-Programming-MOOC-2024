import random

dice = {
    "A": [3, 3, 3, 3, 3, 6],
    "B": [2, 2, 2, 5, 5, 5],
    "C": [1, 4, 4, 4, 4, 4]
}


def roll(die):
    """Rolls the die specified by the argument."""
    return random.choice(dice[die])

def play(die1, die2, times):
    """Throws both dice as many times as specified by the third argument."""
    wins1 = wins2 = ties = 0
    for _ in range(times):
        roll1 = roll(die1)
        roll2 = roll(die2)
        if roll1 > roll2:
            wins1 += 1
        elif roll1 < roll2:
            wins2 += 1
        else:
            ties += 1
    return (wins1, wins2, ties)

if __name__=="__main__":
    
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)
