"""
  1 1 2 3 2 4 2 3 7 7 6  5  4
  0 1 2 3 4
          \   \
         4 - 100, 200
         4 - 200
         100 - 300

         index < k:
            temp +


5 - (100, 4)
2 - (12)
pop()

"""

import collections

class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize
        self.table = collections.defaultdict(list)

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


class CustomStackLee:
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val



a = CustomStackLee(10)
print(a.push(1))
print(a.push(1))
print(a.push(1))
print(a.push(2))
print(a.push(2))
print(a.push(2))
print(a.increment(2,2))
print(a.increment(4,2))
print(a.pop())
print(a.pop())



