
from sortedcontainers import SortedList


class ExamRoom:
    def __init__(self, N: int):
        self.set = SortedList()
        self.n = N

    def seat(self) -> int:
        pos = 0
        if len(self.set) > 0:
            dist = self.set[0]
            prev = -1
            for cur in self.set:
                if prev != -1:
                    d = (cur - prev) // 2
                    if d > dist:
                        dist = d
                        pos = prev + d
                prev = cur
            # check the last chunk
            if (self.n - 1 - self.set[-1]) > dist:
                pos = self.n - 1

        self.set.add(pos)
        return pos

    def leave(self, p: int) -> None:
        if p in self.set:
            self.set.remove(p)




a = ExamRoom(10)
print(a.seat())
print(a.seat())
print(a.seat())
print(a.seat())
print(a.leave(4))
print(a.seat())



