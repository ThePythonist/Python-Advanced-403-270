def func1(*args):
    args = list(args)
    print(args)


func1(10, 20, 30, 60, 50, 40)


def func2(**kwargs):
    print(kwargs)


func2(name="adv 270", students=["zeynab", "amirsam", "mohammad", "arshia"], time=("shanbe", "2 shanbe"))
