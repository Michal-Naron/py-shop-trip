import json

from car import Car
from customer import Customer
from shop import Shop

def shop_trip():
    with open('config.json', 'r') as f:
        data = json.load(f)
        for i in data['customers']:
            customer = Customer(i['name'], i['product_cart'], i['location'], i['money'], Car(i['car']['brand'], i['car']['fuel_consumption']))
            customer.get_money()
            list_of_shopes = []
            for shop in data['shops']:
                shop = Shop(shop['name'], shop['location'], shop["products"])
                list_of_shopes.append(customer.trip_to_shop(shop, data['FUEL_PRICE']))
                the_cheapest_shop = min(list_of_shopes, key=lambda x: x[0])
                if the_cheapest_shop[0] < customer.money:
                    print(f"{customer.name} rides to {the_cheapest_shop[1]}")
                else:
                    print(f"{customer.name} doesn't have enough money to make a purchase in any shop")



