from src.store import Store
from src.products import Product
import random

store1 = Store("We Sell Food and Stuff")

product_object_list = [
    Product("Apples", 1.99, "Fruit"),
    Product("C-3P0s", 2.99, "Cereal"),
    Product("Salmon", 6.99, "Meat"),
    Product("Milk", 3.99, "Dairy"),
    Product("Butter", .50, "Dairy"),
    Product("M&Ms", 1.00, "Candy"),
    Product("Tea", 7.99, "Drinks"),
    Product("Pizza", 7.50, "Frozen"),
    Product("Bananas", 4.19, "Fruit"),
    Product("Yogurt", 3.15, "Dairy"),
    Product("Chicken", 6.15, "Meat")
]

for i in range( len(product_object_list) ):
    x = random.randint(4096, 65535) #Hex values from 1000 to FFFF
    x = hex(x)[2:].upper() #Remove "0x" from beginning, set to all uppercase
    store1.add_product( product_object_list[i], x)

store1.inflation(0.05).set_clearance(0.15)
test_product = Product("Beans", 0.99, "Legumes")
store1.add_product( test_product, "ABCD" )
store1.sell_product("ABCD")

store1.list_products()

store1.list_products("Dairy")