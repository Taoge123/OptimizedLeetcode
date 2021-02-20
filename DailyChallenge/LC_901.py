
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count


class StockSpanner2:
    def __init__(self):
        self.stack = []
        self.prices = []
        self.i = 0

    def next(self, price: int) -> int:
        self.prices.append(price)
        count = 0
        if not self.stack or self.prices[self.stack[-1]] > self.prices[self.i]:
            count = 1
            self.stack.append(self.i)
        else:
            while self.stack and self.prices[self.stack[-1]] <= self.prices[self.i]:
                self.stack.pop()
            if self.stack:
                count = self.i - self.stack[-1]
            else:
                count = self.i + 1
            self.stack.append(self.i)

        self.i += 1
        return count




a = StockSpanner()
print(a.next(100))
print(a.next(80))
print(a.next(60))
print(a.next(70))
print(a.next(60))
print(a.next(75))
print(a.next(85))


