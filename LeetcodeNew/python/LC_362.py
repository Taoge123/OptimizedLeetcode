
"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""

import collections

class HitCounter:
    def __init__(self):
        self.res = 0
        self.hits = collections.deque()

    def hit(self, timestamp: int) -> None:
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp, 1])
        else:
            self.hits[-1][1] += 1
        self.res += 1

    def getHits(self, timestamp: int) -> int:
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.res -= self.hits.popleft()[1]
        return self.res




"""
hit 1
self.hits = [[1, 1]]
self.res = 1

hit 1
self.hits = [[1, 2]] 
self.res = 2

hit 3
self.hits = [[1, 2], [3, 1]]
self.res = 3

hit 4 
self.hits = [[1, 2], [3, 1], [4, 1]]
self.res = 4

hit 303
self.hits = [[1, 2], [3, 1], [4, 1], [303, 1]]
self.res = 5

getHit 303
self.hits = [[3, 1], [4, 1], [303, 1]]
self.res -= 2
"""


a = HitCounter()
print(a.hit(1))
print(a.getHits(2))
print(a.hit(2))
print(a.getHits(2))
print(a.hit(3))
print(a.getHits(3))
print(a.getHits(300))
print(a.getHits(301))




