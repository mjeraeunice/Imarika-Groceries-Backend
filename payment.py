class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total
class Payment:
    def __init__(self):
        self.ordering = []
    def make_payment(self, customer, total):
        if customer.balance < total:
            return "Your accunt balance is insufficient"
        else:
            customer.balance -= total
            order = Order(customer, total)
            self.ordering.append(order)
            return "Your Transaction was successful"
