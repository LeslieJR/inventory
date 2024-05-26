""" Project Description:
Develop a command-line application to manage inventory for a small business. 
This system should allow the user to add new products, update existing product quantities, and delete products. 
It should also provide functionality to display the inventory and visualize inventory data through plots.
"""
from product import Product
class Inventory(Product):
    def __init__(self):
        self.products = []

    def add_product(self, new_product):
        if len(self.products)==0 :
            self.products.append(new_product)
            print(f"New product added successfully. Product name: {new_product.name}")
        else:
            for product in self.products:
                if product.name == new_product.name:
                    print(f"Product {new_product.name} already exists.")
                    return
            self.products.append(new_product)
            print(f"New product added successfully. Product name: {new_product.name}")

    def get_product(self, name):
        for product in self.products:
                if product.name == name:
                    return product
                else: return

    def update_product(self, name, quantity=None, price=None):
        product = self.get_product(name)
        if product:
            product.update(price, quantity)
            print(f"Product named {name} successfully updated")
        else: 
            print(f"Product named {name} was not found")
        
    def delete_product(self, name):
        total_count=len(self.products)
        self.products = [product for product in self.products if product.name != name] 
        if len(self.products) < total_count:
            print(f"Product {name} was deleted successfully")
        else:
            print(f"Product {name} could not be deleted as it was not found")

    def list_inventory(self):
        print("{:<20} {:<10} {:<10}".format('Product Name', 'Quantity', 'Price'))
        print("-" * 40)
        for product in self.products:
            print("{:<20} {:<10} €{:<10.2f}".format(product.name, product.quantity, product.price))
        
        return self.products
    