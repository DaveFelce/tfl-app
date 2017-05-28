class Card:

    def __init__(self, initial_amount=0):
        self.funds = initial_amount

    def can_pay(self, amount):
        return True if (self.funds - amount >= 0) else False


