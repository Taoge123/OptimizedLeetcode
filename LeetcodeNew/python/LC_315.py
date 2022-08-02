"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/208385/Python-three-methods%3A-binary-index-tree-binary-search-tree-segment-tree
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/408322/Python-Different-Concise-Solutions

315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

You are given an integer array nums and you have to return a new counts array.
he counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""
import bisect

"""
-x = ~x + 1 x & (-x) -> lowest bit (two’s complement)

Nums = [5, 2, 6, 1] 
Ranks = [3, 2, 4, 1] 
1, 6, 2, 5 
1, 4, 2, 3 
Nums = [0, 0, 0, 0, 0] 
Nums = [0, 1, 0, 0, 0], 4 => presum(num[:4]) = 1 
Nums = [0, 1, 0, 0, 1] 2 => presum(num[:2]) = 1 
Nums = [0, 1, 1, 0, 1] 3 => presum(num[:3]) = 2 
Nums = [0, 1, 1, 1, 1]
"""

from sortedcontainers import SortedList


class BinaryIndexTree:
    def __init__(self, n):
        self.BIT = [0] * (n + 1)

    def _lowbit(self, i):
        return i & -i

    def update(self, i):
        while i < len(self.BIT):
            self.BIT[i] += 1
            i += self._lowbit(i)

    def query(self, i):
        count = 0
        while i > 0:
            count += self.BIT[i]
            i -= self._lowbit(i)
        return count


class SolutionBIT:
    def countSmaller(self, nums):
        #rank will reduce num to index ex: [2, 6, 3, 7] -> [1, 3, 2, 4]
        rank = {val: i for i, val in enumerate(sorted(set(nums)))}
        n = len(nums)
        tree = BinaryIndexTree(n + 1)
        res = []

        for i in range(n - 1, -1, -1):
            num = rank[nums[i]]
            res.append(tree.query(num))
            tree.update(num+1)
        return res[::-1]




class Solution:
    def countSmaller(self, nums):
        tree = SortedList()
        res = []

        for num in reversed(nums):
            res.append(tree.bisect_left(num))
            tree.add(num)
        return res[::-1]


class SegmentTreeNode:
    def __init__(self, val, start, end):
        self.val = val
        self.start, self.end = start, end
        self.left, self.right = None, None

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.buildTree(0, n-1)

    def buildTree(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root
        mid = (start+end) / 2
        root.left, root.right = self.buildTree(start, mid), self.buildTree(mid+1, end)
        return root

    def update(self, i, diff, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return
        root.val += diff
        if i == root.start == root.end:
            return
        self.update(i, diff, root.left)
        self.update(i, diff, root.right)

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return self.sum(start, end, root.left) + self.sum(start, end, root.right)


class Solution22:
    def countSmallerSegmentTree(self, nums):
        tree, res = SegmentTree(len(nums)), []
        num_rank = {v : i for i, v in enumerate(sorted(nums))}
        for i in reversed(range(len(nums))):
            total = tree.sum(0, num_rank[nums[i]]-1)
            res.append(total)
            tree.update(num_rank[nums[i]], 1)
        return res[::-1]


    # The number we search is guarantee to be in the array
    def index(self, nums, x):
        return bisect.bisect_left(nums, x)

    def countSmallerSegmentTreeBS(self, nums):
        seg_tree, res = SegmentTree(len(nums)), []
        sorted_nums = sorted(nums)
        for i in reversed(range(len(nums))):
            idx = self.index(sorted_nums, nums[i])
            total = seg_tree.sum(0, idx-1)
            res.append(total)
            seg_tree.update(idx, 1)
        return res[::-1]





class Solution1:
    def countSmaller(self, nums):
        arr = []
        res = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(arr, num)
            res.append(idx)
            arr.insert(idx, num)
        return res[::-1]



class Solution2:
    def countSmaller(self, nums):
        nums = nums[::-1]
        nums = [(num, i) for i, num in enumerate(nums)]
        res = [0] * len(nums)

        self.mergesort(nums, 0, len(nums) - 1, res) if nums else None
        return res[::-1]

    def mergesort(self, nums, left, right, res):
        if left == right:
            return
        mid = (left + right) // 2
        self.mergesort(nums, left, mid, res)
        self.mergesort(nums, mid + 1, right, res)

        i = left
        # O(n)
        for j in range(mid + 1, right + 1):
            while i < mid + 1 and nums[i][0] < nums[j][0]:
                i += 1
            res[nums[j][1]] += i - left
        nums[left:right + 1] = sorted(nums[left:right + 1])




nums = [5, 2, 6, 1]
a = Solution()
print(a.countSmaller(nums))



