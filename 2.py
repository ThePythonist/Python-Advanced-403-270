import random
import time
import os


def generate_password():
    digits = []
    for i in range(6):
        x = random.randint(0, 9)
        digits.append(str(x))

    password = "".join(digits)
    return password


while True:
    print(f"========== Your password : {generate_password()} ==========")
    time.sleep(6)
    os.system("cls")
