
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

import collections

class MovingAverage:
    def __init__(self, size):

        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue)) / len(queue)


