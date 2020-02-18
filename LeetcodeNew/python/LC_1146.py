import collections
import bisect


class SnapshotArray:
    def __init__(self, length):
        self.nums = {}
        self.snaps = []

    def set(self, index, val):
        self.nums[index] = val

    def snap(self):
        self.snaps.append(self.nums.copy())
        return len(self.snaps) - 1

    def get(self, index, snap_id):
        if index in self.snaps[snap_id]:
            return self.snaps[snap_id][index]
        else:
            return 0





class SnapshotArrayLee:
    def __init__(self, length: int):
        self.nums = [[[-1, 0]] for i in range(length)]
        self.snapID = 0
        self.n = length

    def set(self, index: int, val: int) -> None:
        self.nums[index].append([self.snapID, val])

    def snap(self) -> int:
        self.snapID += 1
        return self.snapID - 1

    def get(self, index: int, snap_id: int) -> int:
        pos = bisect.bisect_left(self.nums[index], [snap_id + 1]) - 1
        return self.nums[index][pos][1]

a = SnapshotArray(10)
print(a.set(1, 11))
print(a.set(2, 22))
print(a.set(3, 33))
print(a.snap())
print(a.get(1, 1))

