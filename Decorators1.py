# def increase(x):
#     return x + 1
#
#
# def decrease(x):
#     return x - 1
#
#
# def operate(func, x):  # avali taabe - dovomi adad
#     result = func(x)  # khoroji ejraye taabe be ezaye arguman
#     return result
#
#
# print(operate(increase, 10))

def prettier(taabe):  # Decorator
    def wrapper():
        print("----------------")
        taabe()
        print("----------------")

    return wrapper


# def say_hello():
#     print("Hello!")


# d = prettier(say_hello)
# d()


@prettier
def say_hello():
    print("Hello!")


def say_goodbye():
    print("Goodbye!")


say_hello()
say_goodbye()
