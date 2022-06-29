class Pub:
    def __init__(self, _name, _cash):
        self.name = _name
        self.cash = _cash

    def change_till(self, amount):
        self.cash += amount

    def check_age(self, customer):
        return customer.age > 18

    def check_too_drunk(self, customer):
        return customer.drunkness < 10
