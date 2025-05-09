import math


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_of_fuel_in_one_way(self,customer_location: list ,shop_location:list):
        return round(math.sqrt((customer_location[0] - shop_location[0]) ** 2 + (customer_location[1] - shop_location[1]) ** 2) /100 * self.fuel_consumption * 2, 2 )