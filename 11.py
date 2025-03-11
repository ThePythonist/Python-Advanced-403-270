def find_student(**kwargs):
    if "alireza" in kwargs["students"]:
        print(True)
    else:
        print(False)


find_student(
    name="adv 270",
    students=["zeynab", "amirsam", "mohammad", "arshia"],
    time=("shanbe", "2 shanbe")
)
