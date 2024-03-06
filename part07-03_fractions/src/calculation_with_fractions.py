from fractions import Fraction

def fractionate(amount: int):
    # Create an empty list to store the fractions
    fractions = []

    # Loop for the number of parts
    for _ in range(amount):
        # Create a fraction representing 1/amount
        fraction = Fraction(1, amount)

        # Add the fraction to the list
        fractions.append(fraction)

    # Return the list of fractions
    return fractions

if __name__ == "__main__" :
    print(fractionate(5))
