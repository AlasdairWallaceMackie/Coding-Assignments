
class Store:
    def __init__(self, name, product_list = {}):
        if name == None:
            print("Please provide a store name")
            return False

        self.name = name
        self.product_list = product_list

    ###

    line = "--------------------------------------------"

    ###

    def add_product(self, new_product, unique_id):
        self.product_list.update({unique_id: new_product})
        return self
    
    def sell_product(self, unique_id):
        print(self.line)
        print("PRODUCT SOLD:")
        print( self.product_list[unique_id].return_info() )
        print(self.line)
        self.product_list.pop(unique_id)
        return self

    def inflation(self, percent_increase):
        for product in self.product_list:
            self.product_list[product].update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount=0):
        if category == None:
            print("Please provide a category in order to set clearance discount")
        for product in self.product_list:
            if( self.product_list[product].category == category ):
                self.product_list[product].update_price(percent_discount, False)
        return self

    def list_products(self, category = None):
        print(self.line)
        print(f'"{self.name}" PRODUCT LIST')
        if category != None:
            print("Category: " + category)
        print(self.line)
        for product in self.product_list:
            if category == None or self.product_list[product].category == category:
                print(product + ": " + self.product_list[product].return_info() )
        print(self.line)
        return self


print("Store.py initialized")

