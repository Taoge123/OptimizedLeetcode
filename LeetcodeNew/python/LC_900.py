
import collections

class RLEIterator:

    def __init__(self, A):
        self.queue = collections.deque(A)

    def next(self, n):
        while self.queue and n > self.queue[0]:
            n -= self.queue.popleft()
            self.queue.popleft()
        if not self.queue:
            return -1
        res = self.queue[1]
        self.queue[0] -= n
        return res



class RLEIterator2:
    def __init__(self, A):
        self.nums = A
        self.i = 0

    def next(self, n: int) -> int:
        while self.i < len(self.nums):
            if n > self.nums[self.i]:
                n -= self.nums[self.i]
                self.i += 2

            else:
                self.nums[self.i] -= n
                return self.nums[self.i + 1]
        return -1
