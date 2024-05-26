class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def update(self, price=None, quantity=None):
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if price is not None and quantity is not None:
            self.price = price
            self.quantity = quantity
    
    def __str__(self):
        return '(Product: %s, price: %s, quantity: %s)' % (self.name, self.price, self.quantity)
