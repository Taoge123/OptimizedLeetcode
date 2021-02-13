import collections


class MyCalendarThree:

    def __init__(self):
        self.count = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.count[start] += 1
        self.count[end] -= 1

        res = 0
        cur = 0
        for time in sorted(self.count):
            cur += self.count[time]
            if cur > res:
                res = cur

        return res


