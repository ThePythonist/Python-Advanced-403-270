import random


def irancell():
    prefix = ["0930", "0939", "0933", "0936"]
    pn = f"{random.choice(prefix)}"

    for i in range(7):
        pn += str(random.randint(0, 9))

    return pn


def hamrahaval():
    prefix = ["0912", "0911", "0919", "0993"]
    pn = f"{random.choice(prefix)}"

    for i in range(7):
        pn += str(random.randint(0, 9))

    return pn


def rightel():
    prefix = ["0921", "0922", "0923"]
    pn = f"{random.choice(prefix)}"

    for i in range(7):
        pn += str(random.randint(0, 9))

    return pn
