"""
315. Count of Smaller Numbers After Self
327. Count of Range Sum
493. Reverse Pairs

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2 * nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
"""
More explanation for the BIT-based solution:

We want the elements to be sorted so there is a sorted version of the input array which is copy.

The bit is built upon this sorted array. Its length is one greater than that of the copy array to account for the root.

Initially the bit is empty and we start doing a sequential scan of the input array. For each element being scanned, 
we first search the bit to find all elements greater than twice of it and add the result to res. 
We then insert the element itself into the bit for future search.

Note that conventionally searching of the bit involves traversing towards the root from some index of the bit, 
which will yield a predefined running total of the copy array up to the corresponding index. 
For insertion, the traversing direction will be opposite and go from some index towards the end of the bit array.

For each scanned element of the input array, its searching index will be given by the index of the first element in the copy array 
that is greater than twice of it (shifted up by 1 to account for the root), 
while its insertion index will be the index of the first element in the copy array that is no less than itself 
(again shifted up by 1). This is what the index function is for.

For our case, the running total is simply the number of elements encountered during the traversal process. 
If we stick to the convention above, the running total will be the number of elements smaller than the one at the given index, 
since the copy array is sorted in ascending order. However, we'd actually like to find the number of elements greater than some value 
(i.e., twice of the element being scanned), therefore we need to flip the convention. 
This is what you see inside the search and insert functions: the former traversing towards the end of the bit while the latter towards the root.
"""
"""
1 1 2 3 3

1 -> 2 
2 -> 3
3 -> 5

update(2,1) -> BIT: 0 0 1 0 1 0

update(5,1) -> BIT: 0 0 1 0 1 1

update(3,1) -> BIT: 0 0 1 1 2 1

update(5,1) -> BIT: 0 0 1 1 2 2

update(2,1) -> BIT: 0 0 2 1 3 2





"""

import bisect


class BinaryIndexTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def _lowbit(self, i):
        return i & -i

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.sums[i]
            i -= self._lowbit(i)
        return res


class Solution:
    def reversePairs(self, nums):
        newNums = nums + [num * 2 for num in nums]
        sortNums = sorted(list(set(newNums)))
        tree = BinaryIndexTree(len(sortNums))
        res = 0
        ranks = {}
        for i, n in enumerate(sortNums):
            ranks[n] = i

        for num in nums[::-1]:
            #如果num被更新了，num * 2加入tree里面
            res += tree.query(ranks[num])
            tree.update(ranks[num * 2] + 1, 1)
        return res


"""
nums     = [1, 3, 2, 3, 1] = [1,3,2,3,1,2,6,4,6,2] = [1,2,3,4,6]
newNums  = [1, 3, 2, 3, 1, 2, 6, 4, 6, 2]
sortNums = [1, 2, 3, 4, 6]
rank =     [0, 1, 2, 3, 4]
tree:
[0, 0, 0, 0, 0, 0]
1
[0, 0, 1, 0, 1, 0]
3
[0, 0, 1, 0, 1, 1]
2
[0, 0, 1, 0, 2, 1]
3
[0, 0, 1, 0, 2, 2]
1
[0, 0, 2, 0, 3, 2]




"""
class Solution11:
    def reversePairs(self, nums) -> int:
        res = 0
        arr = []
        for i in range(len(nums)):
            index = bisect.bisect_right(arr, 2 * nums[i])
            res += (i - index)
            bisect.insort(arr, nums[i])
        return res





class Solution2:
    def __init__(self):
        self.res = 0

    def reversePairs(self, nums):
        self.mergeSort(nums)
        return self.res

    def mergeSort(self, nums):
        # merge sort body
        n = len(nums)
        if n <= 1:  # base case
            return nums
        else:  # recursive case
            left = self.mergeSort(nums[:int(n / 2)])
            right = self.mergeSort(nums[int(n / 2):])
            return self.merge(left, right)

    def merge(self, left, right):
        # merge
        i, j = 0, 0  # increase l and r iteratively
        while i < len(left) and j < len(right):
            if left[i] <= 2 * right[j]:
                i += 1
            else:
                self.res += len(left) - i  # add here
                j += 1
        return sorted(left + right)  # I can't avoid TLE without timsort...




class Solution3:
    def reversePairs(self, nums):
        if len(nums) <= 1:
            return 0
        self.res = 0
        self.merge(nums)
        return self.res

    def merge(self, nums):
        if len(nums) <= 1:
            return nums

        left = self.merge(nums[:len(nums) // 2])
        right = self.merge(nums[len(nums) // 2:])
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= 2 * right[j]:
                i += 1
            else:
                self.res += len(left) - i
                j += 1

        return sorted(left + right)


nums = [1,3,2,3,1]
a = Solution()
print(a.reversePairs(nums))


