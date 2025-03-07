import jdatetime

thisyear = jdatetime.datetime.now().year
birthyear = int(input("Enter your birth year : "))
age = thisyear - birthyear
print(f"You are {age} years old")