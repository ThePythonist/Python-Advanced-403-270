import time
from tools.functions import average

s1 = []
s2 = []


def tictoc(func):  # Decorator
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        runtime = t2 - t1
        print(f"Function {func.__name__} took {runtime} seconds to execute")
        print("-" * 100)

        if func.__name__ == "solution1":
            s1.append(runtime)
        else:
            s2.append(runtime)

    return wrapper


@tictoc
def solution1():
    c = 0

    for i in range(5000000):
        c += 1

    # print(c)


@tictoc
def solution2():
    c = 0

    while c < 5000000:
        c += 1

    # print(c)


for i in range(10):
    solution1()
    solution2()

print(average(*s1))
print(average(*s2))
