


"""
https://www.youtube.com/watch?v=yCQN096CwWM

Given a non-empty 2D matrix matrix and an integer k,
find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:

Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
"""

"""
The idea comes from the C++ or Java solution posted on discuss, I just rewrite the idea with python.

1. using two pointers to scan the column, Space is O(col)
2. left and right both start from the 0, and move right first when it reaches the end then move left
3. record the sum of the value and find the max sum less than k
4. the following code can also be used to solve Max Sum of Sub-Matrix, 
   only need to replace the maxSubArraylessK with Kadane's algorithm
"""

"""
这个算法巧妙在把二维数组按行或列拆成多个一维数组，然后利用一维数组的累加和来找符合要求的数字，
这里用了lower_bound来加快我们的搜索速度，也可以使用二分搜索法来替代。我们建立一个集合set，然后开始先放个0进去，
为啥要放0呢，因为我们要找lower_bound(curSum - k)，当curSum和k相等时，0就可以被返回了，这样我们就能更新结果了。
由于我们对于一维数组建立了累积和，那么sum[i,j] = sum[i] - sum[j]，其中sums[i,j]就是目标子数组需要其和小于等于k，
然后sums[j]是curSum，而sum[i]就是我们要找值，当我们使用二分搜索法找sum[i]时，sum[i]的和需要>=sum[j] - k，
所以也可以使用lower_bound来找
"""
import bisect

class Solution1:
    def maxSubArraylessK(self, nums, k):
        """
        we need to find the sum[right]-sum[left]<=k since the bitsect return the index of the sorted value
        we can't directly pop the nums[idx] we should use insort from the bisect
        """
        # python set() doesn't support indexing, using list instead

        cumset = []
        cumset.append(0)
        maxsum = -1 << 32
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            # find the lower bound of the index
            idx = bisect.bisect_left(cumset, cursum - k)
            # find max in sum[right]-sum[left]<=k
            if 0 <= idx < len(cumset):
                maxsum = max(maxsum, cursum - cumset[idx])
            # using insort instead of append since bisect_left reason
            bisect.insort(cumset, cursum)
        return maxsum


    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        """
        The python solution hasn't a good time performance,
        since lack some of the datatype to do 
        I am trying to imitate the way solved in c++ or Java
        Ther related quesiton might be:
        1. #53. Maximum Subarray 
        2. Maximum Subarray sum less or equal than K
        3. maximun sum of rectangle 
        """
        if not matrix or not matrix[0]:
            return 0
        row, col = len(matrix), len(matrix[0])
        res = -(1 << 32)
        # using two pointer to record the scan position
        for left in range(col):
            # reset mem to store the row data
            cursums = [0 for _ in range(row)]
            # since the rectange has area>0
            right = left
            while right < col:
                # count one row
                for i in range(row):
                    cursums[i] += matrix[i][right]
                # find the max in this row
                curarrmax = self.maxSubArraylessK(cursums, k)
                res = max(res, curarrmax)
                right += 1

        return res















