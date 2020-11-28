"""
X X X X X X X X X i

A: [Y Y Y Y Y Z Z Z Z Z]
B: [Y Y Y Y Y] C : [Z Z Z Z Z]
if B is sorted, so we can easily use binary search to find small value in B for each value in C



"""

from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions) -> int:
        mod = 10 ** 9 + 7
        res = 0
        nums = SortedList()

        for i, num in enumerate(instructions):
            left = nums.bisect_left(num)
            right = nums.bisect_right(num)
            res += min(left, len(nums) - right)
            nums.add(num)

        return res % mod


class BinaryIndexTree:
    def __init__(self, n):
        self.BIT = [0] * (n + 1)

    def _lowbit(self, i):
        return i & -i

    def query(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= i & -i
        return count

    def update(self, i):
        while i < len(self.BIT):
            self.BIT[i] += 1
            i += i & -i


class SolutionBIT:
    def createSortedArray(self, instructions) -> int:
        n = max(instructions)
        mod = 10 ** 9 + 7
        tree = BinaryIndexTree(n)

        res = 0
        for i, num in enumerate(instructions):
            res += min(tree.query(num - 1), i - tree.query(num))
            tree.update(num)
            # print(tree.BIT)
        return res % mod




