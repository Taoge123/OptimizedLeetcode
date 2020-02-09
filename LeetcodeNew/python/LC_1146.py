import collections
import bisect


class SnapshotArray:
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

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


