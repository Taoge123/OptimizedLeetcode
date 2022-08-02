"""
https://leetcode.com/problems/count-good-triplets-in-an-array/discuss/1787085/BIT
https://leetcode.cn/problems/count-good-triplets-in-an-array/solution/shu-zhuang-shu-zu-xian-duan-shu-ping-hen-knho/


Similar questions:
1713.Minimum-Operations-to-Make-a-Subsequence
1534. Count Good Triplets

"""


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

    def update(self, i, val):
        while i < len(self.BIT):
            self.BIT[i] += val
            i += i & -i

class Solution:
    def goodTriplets(self, nums1, nums2) -> int:

        n = len(nums1)
        tree = BinaryIndexTree(n)
        rank = {}
        for i in range(n):
            rank[nums2[i]] = i + 1

        res = 0
        for i in range(n):
            pos = rank[nums1[i]]
            left = tree.query(pos)
            right = n - pos - (tree.query(n) - tree.query(pos))
            # right = n - pos - (tree.query(n) - left) # faster
            res += left * right
            tree.update(pos, 1)
        return res



