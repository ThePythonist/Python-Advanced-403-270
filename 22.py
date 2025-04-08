class Product:
    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price


class ShoppingCart:
    def __init__(self, id, user):
        self.id = id
        self.user = user
        self.products = []
        self.total = 0

    def addToBasket(self, product):
        self.products.append(product)
        self.total += product.price
        print(f"Added {product.name} to basket")
        print("=" * 100)

    def removeFromBasket(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total -= product.price
            print(f"Removed {product.name} from basket")
            print("=" * 100)
        else:
            print("Product is not in the basket")
            print("=" * 100)

    def showFactor(self):
        print(f"Basket Products : {[i.name for i in self.products]}")
        print(f"Total amount : {self.total}")


prd1 = Product("SAMSUNG A05", "13589666", 9899000)
prd2 = Product("SONY mdr-ex14", "14498156", 299000)
prd3 = Product("VERNA W49 Ultra", "14387612", 775000)

bsk1 = ShoppingCart("01101", "Hamed")
bsk2 = ShoppingCart("01102", "Arman")
bsk3 = ShoppingCart("01103", "Peyman")

bsk1.addToBasket(prd3)
bsk1.addToBasket(prd3)
bsk1.addToBasket(prd2)
bsk1.addToBasket(prd1)
bsk1.showFactor()
bsk1.removeFromBasket(prd2)
bsk1.removeFromBasket(prd2)
bsk1.showFactor()
