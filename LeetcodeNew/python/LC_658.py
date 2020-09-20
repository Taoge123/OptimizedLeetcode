"""
658. Find K Closest Elements
类型：考虑边界
Time Complexity (logN + K)
Time Spent on this question: 40 mins
high level思路：这道题可以理解为 Leetcode 35. Search Insert Position 的Follow Up。首先先写一个和35题一模一样的辅助方程，用来寻找插入的位置。位置锁定以后，比对该位置的左边和右边的值。

实践：关于比对值，我之前的思路是开辟一个Array，然后在对比完大小后，往这个Array一个一个的加，后来选择用Two Pointer来表示L和R的指针，
然后运用Python的Indexing节省了一小部分的空间。另外要注意的一个细节就是，我们找到的这个插入点，并不代表我们找到和题目中x一样的值，所以在比对的时候，我们一定要记住用x和插入点的值比对:

if x - arr[l-1] <= arr[r] - x:

这里我并没有写arr[r + 1] 就是这个原因。还有一个细节就是我之前定义l 和r的时候用的以下代码:

l, r = index - 1, index

遇到的问题就是过不了当arr等于1的Edge case，理由是因为提前处理index会导致while循环进不去。因为当arr长度和k等于1的时候，r-l就等于k了。所以我最终没有提前修改l的位置，是在循环里面处理的这个Edge:

if x - arr[l-1] <= arr[r] - x:

"""
"""
Intuition
The array is sorted.
If we want find the one number closest to x,
we don't have to check one by one.
it's straightforward to use binary research.

Now we want the k closest,
the logic should be similar.


Explanation:
Assume we are taking A[i] ~ A[i + k - 1].
We can binary research i
We compare the distance between x - A[mid] and A[mid + k] - x

If x - A[mid] > A[mid + k] - x,
it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
and we have mid smaller than the right i.
So assign left = mid + 1.

Note that, you SHOULD NOT compare the absolute value of abs(x - A[mid]) and abs(A[mid + k] - x).
It fails at cases like A = [1,1,2,2,2,2,2,3,3], x = 3, k = 3

The problem is interesting and good.
Unfortunately the test cases is terrible.
The worst part of Leetcode test cases is that,
you sumbit a wrong solution but get accepted.

You didn't read my post and upvote carefully,
then you miss this key point.


Time Complexity:
O(log(N - K)) to binary research and find result
O(K) to create the returned list.
"""

import bisect


class SolutionCsp:
    def findClosestElements(self, arr, k: int, x: int):
        left, right = 0, len(arr) - k

        while left < right:
            mid = (right - left) // 2 + left
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]



class SolutionLee:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1]
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


class SolutionGongJin:
    def findClosestElements(self, arr, k, x):
        index = self.findIndex(arr, x)
        l, r = index, index

        while r - l < k:
            if l == 0:
                return arr[:k]
            if r == len(arr):
                return arr[-k:]
            if x - arr[l - 1] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        return arr[l:r]

    def findIndex(self, arr, target):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l



class SolutionSquareMichael:
    def findClosestElements(self, arr, k, x):
        if not arr or k <= 0:
            return []

        n = len(arr)
        while len(arr) > k:
            if abs(arr[0] - x) > abs(arr[-1] - x):
                arr.pop(0)
            else:
                arr.pop(-1)
        return arr
