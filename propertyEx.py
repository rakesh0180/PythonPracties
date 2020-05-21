class Product:
    def __init__(self, price):
        self.set_price(price)

    def set_price(self, value):
        if value < 0:
            raise ValueError("price must be greater than zero")
        self._price = value

    def get_price(self):
        return self._price

    # propertie tag
    price = property(set_price, get_price)


prod = Product(-50)
