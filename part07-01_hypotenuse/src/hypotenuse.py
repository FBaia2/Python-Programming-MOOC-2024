import math
def hypotenuse(leg1: float, leg2: float):
    mathings = math.pow(leg1,2) + math.pow(leg2,2)
    return math.sqrt(mathings)




if __name__=="__main__":
    print(hypotenuse(3,4)) # 5.0