import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        data = json.load(f)
        for customer_data in data["customers"]:
            customer = Customer(
                customer_data["name"],
                customer_data["product_cart"],
                customer_data["location"],
                customer_data["money"],
                Car(
                    customer_data["car"]["brand"],
                    customer_data["car"]["fuel_consumption"]
                )
            )
            customer.get_money()
            list_of_shops = []
            for shop_data in data["shops"]:
                shop = Shop(
                    shop_data["name"],
                    shop_data["location"],
                    shop_data["products"]
                )
                trip_cost = customer.trip_to_shop(shop, data["FUEL_PRICE"])
                list_of_shops.append(trip_cost)
            the_cheapest = min(list_of_shops, key=lambda x: x[0])
            if the_cheapest[0] < customer.money:
                print(f"{customer.name} rides to {the_cheapest[1].name}")
            else:
                print(f"{customer.name} can't afford any shop")
                continue
            print("\nDate: 04/01/2021 12:33:41")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            customer.list_of_bought_stuff(the_cheapest[1])
            print(f"\n{customer.name} rides home")
