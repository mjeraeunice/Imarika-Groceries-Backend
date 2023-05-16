class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

class CustomerService:
    def __init__(self):
        self.orders = []

    def place_order(self, customer, products):
        order = Order(customer, products)
        self.orders.append(order)
        return order