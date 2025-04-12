class Calculator:
    def __init__(self, n1, op, n2):
        self.num1 = n1
        self.num2 = n2
        self.operator = op

    def add(self):
        print(self.num1 + self.num2)

    def subtract(self):
        print(self.num1 - self.num2)

    def multiply(self):
        print(self.num1 * self.num2)

    def divide(self):
        print(self.num1 / self.num2)


def main():
    n1 = int(input("Enter first number : "))
    op = input("Enter operator : ")
    n2 = int(input("Enter second number : "))

    calc = Calculator(n1, op, n2)
    print("Result", end=" : ")

    if op == "+":
        calc.add()
    elif op == "-":
        calc.subtract()
    elif op == "*":
        calc.multiply()
    elif op == "/":
        calc.divide()
    else:
        print("Invalid operator")
        main()


main()
