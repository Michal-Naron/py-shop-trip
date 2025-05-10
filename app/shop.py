from typing import Dict, List


class Shop:
    def __init__(
        self,
        name: str,
        location: List[float],
        products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase(self, product_cart: Dict[str, int]) -> float:
        price = 0.0
        for product, quantity in product_cart.items():
            if product in self.products:
                price += quantity * self.products[product]
        return round(price, 2)
