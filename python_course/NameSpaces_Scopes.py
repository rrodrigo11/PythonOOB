# -*- coding: utf-8 -*-
import datetime

#used to print all the module namespace
for name in sorted(datetime.__dict__):
    print(name)

import uuid

#**********************************************************
class Product:

    def __init__(self, product_name, product_id, price):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]

#used to display the 'Product' class namespace
for name in Product.__dict__:
    print(name)


product = Product('Mobile Phone', '54274', 2900)
#used to display the namespace of the instance 'product' of class 'Product'
print(product.__dict__)