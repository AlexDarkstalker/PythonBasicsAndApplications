class MoneyBox:
    capacity = 0
    amount = 0

    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity - v >= self.amount

    def add(self, v):
        self.amount += v
