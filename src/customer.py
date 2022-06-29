class Customer:
    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drunkness = 0

    def buy_drink(self, drink, pub):
        if pub.check_age(self) and pub.check_too_drunk(self):
            self.wallet -= drink.price
            pub.change_till(drink.price)
            self.increase_drunkness(drink)

    def increase_drunkness(self, drink):
        self.drunkness += drink.alcohol_level

    def buy_food(self, food, pub):
        self.drunkness -= food.rejuvenation_level
        self.wallet -= food.price
        pub.change_till(food.price)
