from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase(self, product_cart: dict) -> float:
        price = 0
        for key, value in product_cart.items():
            for key2, value2 in self.products.items():
                if key == key2:
                    price += value * value2
        return round(price, 2)