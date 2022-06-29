class Pub:
    def __init__(self, _name, _cash):
        self.name = _name
        self.cash = _cash
        self.stock = {}

    def change_till(self, amount):
        self.cash += amount

    def check_age(self, customer):
        return customer.age > 18

    def check_too_drunk(self, customer):
        return customer.drunkness < 10

    def change_stock_count(self, drink):
        self.stock[drink] -= 1

    def add_drink_to_stock(self):
        self.stock

    def check_stock_value(self):
        total_val = 0
        for item in self.stock:
            total_val += (item.price * self.stock[item])
        return total_val
