import collections

class StockSystem:
    def __init__(self, capacity):
        self.min_dq = collections.deque([])
        self.max_dq = collections.deque([])
        self.capacity = capacity
        self.count = 0

    def input(self, num):
        self.count += 1
        i = self.count
        while self.min_dq and self.min_dq[-1][0] >= num:
            self.min_dq.pop()
        self.min_dq.append((num, i))
        if i - self.min_dq[0][1] + 1 > self.capacity:
            self.min_dq.popleft()

        while self.max_dq and self.max_dq[-1][0] <= num:
            self.max_dq.pop()
        self.max_dq.append((num, i))
        if i - self.max_dq[0][1] + 1 > self.capacity:
            self.max_dq.popleft()
        return self.min_dq[0][0], self.max_dq[0][0]


a = StockSystem(2)
for i in [1, 2, 1,4,3,1,2,3,4,1,2,1,3,4,2,]:
    print(a.input(i))