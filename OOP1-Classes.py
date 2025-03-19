class SedanCar:  # PascalCase
    def __init__(self, n, c, m):
        self.name = n
        self.color = c
        self.model = m

    def startEngine(self):  # camelCase
        print("STARTED ENGINE")

    def accelerate(self):
        print("ACCELERATED")

    def brake(self):
        print("BRAKE")

    def horn(self):
        print("BOOOOOOOOOOGH")


# Creating instance (objects)
car1 = SedanCar("runna", "blue", 1401)
car2 = SedanCar("samand", "white", 1399)
car3 = SedanCar("dena", "black", 1403)

print(car1.color)
