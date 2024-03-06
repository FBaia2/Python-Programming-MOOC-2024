import string
from random import randint
def generate_password(num: int):
    new_rnd = []
    nutz = []
    p_word = []
    real = []
    deez = ""
    deez = string.ascii_lowercase
    for i in deez:
        nutz.append(i)

    while len(p_word) < num:
        new_rnd = randint(0, len(nutz))
        p_word.append(new_rnd)

    for n in p_word:
        real.append(nutz[n -1])
    realest = "".join(real)

    return realest
    



if __name__=="__main__":
    for i in range(10):
        print(generate_password(8))