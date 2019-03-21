"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms

Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import bisect
import heapq

"""
给定一个 n x n 矩阵，其中每一行每一列都按照递增序排列，寻找矩阵中的第k小元素。

注意是要寻找排好序的第k小元素，而不是第k个不重复元素。

测试用例如题目描述。

你可以假设k总是有效的， 1 ≤ k ≤ n2
"""
"""
首先将矩阵的左上角（下标0,0）元素加入堆

然后执行k次循环：

弹出堆顶元素top，记其下标为i, j

将其下方元素matrix[i + 1][j]，与右方元素matrix[i][j + 1]加入堆（若它们没有加入过堆）
"""

class Solution1:
    def kthSmallest(self, matrix, k):

        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        visited[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)

            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))

            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))

        return ans


"""
上述解法的优化：
实际上visited数组可以省去，在队列扩展时，当且仅当j == 0时才向下扩展，否则只做横向扩展。
"""
class Solution2:
    def kthSmallest(self, matrix, k):

        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans


"""
将查找上下限设为矩阵的右下角与左上角元素

查找过程中对中值在矩阵每一行的位置进行累加，记该值为loc

根据loc与k的大小关系调整上下限
"""
class SolutionBinerySearch:
    def kthSmallest(self, matrix, k):

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

"""
上述解法的优化：

循环中对每行的二分查找可以替换为：从矩阵左下角到右上角的“阶梯型”遍历。
"""
class SolutionBinerySearch2:
    def kthSmallest(self, matrix, k):

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = self.countLower(matrix, mid)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt


"""
我觉得用二分做最好，这个方法只要求行有序，和列有木有序并没有关系。 
（或者列有序，行有序无序都没关系）

设L = min(matrix) R= max(matrix)  , mid =( L + R ) / 2 ，mid为我们猜测的答案。

然后对于每一行，找它在该行中第几大（也是二分，找上界），累加和K比较。

值得注意的是枚举 答案应该用下界， 因为猜想的解不一定在数组中，不断的收缩直到找到在数组中的元素为止。

查找一行需要log(n) ，有n行所以nlog(n)，最坏下需要查找log(X)次
（X= int最大值的时候logX仅仅才为32），X为最大最小数差值. 所以总复杂度为O(nlogn *  logX)

PS：其实是我一开始看成就行有序→_→，然后就直接二分了
"""

class Solution11:
    def kthSmallest(self, matrix, k):

        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = L + ((R - L) >> 1)
            temp = sum([self.binary_search(row, mid, n) for row in matrix])
            if temp < k:  L = mid + 1
            else:  R = mid
        return L

    def binary_search(self, row, x, n):
        L, R = 0, n
        while L < R:
            mid = (L + R) >> 1
            if row[mid] <= x:
                L = mid + 1
            else:
                R = mid
        return L

"""
上述的解法并没有利用到列有序的性质。

而下面的解法利用了列有序的性质，并将复杂度降到了O(nlogX) 其中X = max – min

我们仍采用猜测法，设L = min(matrix) R= max(matrix) , mid =( L + R ) / 2 ，mid为我们猜测的答案。

对于mid，我们不必再所有的行或列种执行二分查找，我们可以从左下角出发，若matrix[i][j] <= mid，
则下一次查询在右边（j++），并且，该列的所有元素均比mid小，因此可以cnt += (i+1)

对于matrix[i][j] > mid，则 i – – 。 过程类似于240. Search a 2D Matrix II  (题解在最下方)
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        L, R = matrix[0][0], matrix[n - 1][n - 1]
        while L < R:
            mid = L + ((R - L) >> 1)
            temp = self.search_lower_than_mid(matrix, n, mid)
            if temp < k:
                L = mid + 1
            else:
                R = mid
        return L

    def search_lower_than_mid(self, matrix, n, x):
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                j += 1
                cnt += i + 1
            else:
                i -= 1
        return cnt



matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

k = 8

a = Solution1()
print(a.kthSmallest(matrix, k))

