from inventory import Inventory
from product import Product
from plots import plot_inventory_levels, plot_inventory_value
def main():
    """
    Main function to run the inventory management system.
    """
    # Create an instance of Inventory.
    inventory = Inventory()
    
    # Add some initial products to demonstrate the system.
    laptop = Product('Macbook', 1, 2600)
    mobile = Product('Iphone', 5, 1200)
    keyboard = Product('Keyboard', 3, 200)
    
    inventory.add_product(laptop)
    inventory.add_product(mobile)
    inventory.add_product(keyboard)

    # Use an input loop to accept user commands to add, get, update, delete, list, or plot inventory, or exit the program.
    while True:
        command = input("\nEnter command (add, get, update, delete, list, plot, exit): ").strip().lower()

        if command == "add":
            name = input("Enter item name: ").strip()
            quantity = int(input("Enter item quantity: ").strip())
            price = float(input("Enter item price: ").strip())
            inventory.add_product(Product(name, quantity, price))

        elif command == "get":
            name = input("Enter item name: ").strip()
            inventory.get_product(name)

        elif command == "update":
            name = input("Enter item name: ").strip()
            quantity = int(input("Enter new item quantity: ").strip())
            price = float(input("Enter new item price: ").strip())
            inventory.update_product(Product(name, quantity, price))

        elif command == "delete":
            name = input("Enter item name to delete: ").strip()
            inventory.delete_product(name)
           
        elif command == "list":
            inventory.list_inventory()

        elif command == "plot":
            plot_name = input("\nEnter plot name (level or value): ").strip()
            if plot_name == 'level':
                plot_inventory_levels(inventory)
            elif plot_name == 'value':
                plot_inventory_value(inventory)
            else:
               print("Invalid plot name. Please try again.") 

        elif command == "exit":
            print("Exiting the program.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
