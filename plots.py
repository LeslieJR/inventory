"""
Create at least two plots: one for inventory levels and another for the value of the inventory.
"""
import matplotlib.pyplot as plt

def plot_inventory_levels(inventory):
    """
    Visualizes the inventory levels of each product using a bar chart.
    """
    """ Calculate percentage based on quantity """
    products = inventory.list_inventory()
    product_names = []
    product_quantities = []
    for product in products:
        product_names.append(product.name)
        product_quantities.append(product.quantity)

    plt.bar(product_names, product_quantities)
    plt.xlabel('Item Name')
    plt.ylabel('Item Quantity')
    plt.title('Inventory Levels')
    plt.show()
    

def plot_inventory_value(inventory):
    """
    Visualizes the total value of each product in the inventory.
    """
    
    products = inventory.list_inventory()
    product_names = []
    product_total_value = []
    for product in products:
        product_names.append(product.name)
        product_total_value.append(product.quantity*product.price)

    plt.bar(product_names, product_total_value)
    plt.xlabel('Item Name')
    plt.ylabel('Item Total Value (€)')
    plt.title('Inventory Values')
    plt.show()

