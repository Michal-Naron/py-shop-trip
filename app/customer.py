from app.shop import Shop
from  car import Car
from typing import Any
class Customer:
    def __init__(self, name: str, products: dict, location: list, money: float, car: Car) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def get_money(self) -> None:
        print(f'{self.name} has {self.money} dollars')

    def trip_to_shop(self, shop: Shop, fuel_price) -> Any:
        total_cost = 0
        total_cost += self.car.cost_of_fuel_in_one_way(self.location, shop.location) * fuel_price
        total_cost += shop.purchase(self.products)
        print(f"{self.name}'s trip to {shop.name} costs {total_cost}")
        return total_cost, shop.name

