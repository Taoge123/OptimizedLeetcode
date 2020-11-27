
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count

