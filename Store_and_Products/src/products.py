
class Product:
    def __init__(self, name, price, category):
        if name == None or price == None or category == None:
            print("Product creation failed -- missing attributes")
            return False

        self.name = name
        self.price = price
        self.category = category

    ###

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        self.price = round(self.price, 2) #Round to 2 decimal places
        return self
    
    def return_info(self):
        return f"{self.name} | Price: ${self.price} | Category: {self.category}"



print("Products.py initialized")