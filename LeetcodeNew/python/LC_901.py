
"""
Explanation
You can refer to the same problem 739. Daily Temperatures.

Push every pair of <price, result> to a stack.
Pop lower price from the stack and accumulate the count.

One price will be pushed once and popped once.
So 2 * N times stack operations and N times calls.
I'll say time complexity is amortized O(1)

P  = 100 80 60 70 60 75 85
dp =  1  1  1  2  1  4  6

100 1
100 1, 80 1
100 1, 80 1, 60 1
100 1, 80 1, 70 2
100 1, 80 1, 70 2 60 1
100 1, 80 1, 75 4
100 1, 85 6
"""


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]
        self.stack.append((price, count))
        return count



