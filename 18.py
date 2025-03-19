def adder(number):
    if number < 10:
        return number
    else:
        digits = [int(i) for i in str(number)]
        number = sum(digits)
        return adder(number)


print(adder(1545))
