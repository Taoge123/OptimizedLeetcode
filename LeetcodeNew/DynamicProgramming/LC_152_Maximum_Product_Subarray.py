
"""
https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
Calculate prefix product in A.
Calculate suffix product in A.
Return the max.
"""
"""
The first two lines are like writing:

if A[i - 1] != 0:
    A[i] *= A[i - 1]
else:
    A[i] *= 1
if B[i - 1] != 0:
    B[i] *= B[i - 1]
else:
    B[i] *= 1
Notice that the else portion is not needed, I just included it to try to make it more clear.

For the third line, A and B are lists, so A+B returns a list of A appended with all the elements in B. 
Then max just takes the highest value in that list.

The algorithm makes two recursive relationship lists; if it helps think Fibonacci sequence, 
but for multiplication. So F0 = x, where x is the first element and last element in the list. 

Then Fn = Fn-1 * Fn.
"""

class SolutionLee:
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        return max(A + B)


class Solution1:
    def maxProduct(nums):
        maximum = big = small = nums[0]
        for n in nums[1:]:
            big, small = max(n, n * big, n * small), min(n, n * big, n * small)
            maximum = max(maximum, big)
        return maximum


class Solution11:
    def maxProduct(self, A):
        res = small = big = A[0]
        for i in A[1:]:
            small, _, big = sorted([small * i, big * i, i])
            res = max(res, small, big)
        return res


class SolutionCaikehe:
    # O(2*n) space
    def maxProduct1(self, nums):
        if not nums:
            return
        locMin = [0] * len(nums)
        locMax = [0] * len(nums)
        locMin[0] = locMax[0] = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                locMax[i] = max(locMin[i - 1] * nums[i], nums[i])
                locMin[i] = min(locMax[i - 1] * nums[i], nums[i])
            else:
                locMax[i] = max(locMax[i - 1] * nums[i], nums[i])
                locMin[i] = min(locMin[i - 1] * nums[i], nums[i])
            gloMax = max(gloMax, locMax[i])
        return gloMax

    # O(1) space
    def maxProduct2(self, nums):
        if not nums:
            return
        locMin = locMax = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < 0:
                tmp = locMax
                locMax = max(locMin * nums[i], nums[i])
                locMin = min(tmp * nums[i], nums[i])
            else:
                locMax = max(locMax * nums[i], nums[i])
                locMin = min(locMin * nums[i], nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax

    # O(1) space
    def maxProduct(self, nums):
        if not nums:
            return
        locMin = locMax = gloMax = nums[0]
        for i in xrange(1, len(nums)):
            tmp = locMin
            locMin = min(locMin * nums[i], nums[i], locMax * nums[i])
            locMax = max(tmp * nums[i], nums[i], locMax * nums[i])
            gloMax = max(gloMax, locMax)
        return gloMax


"""
Maximum Product Subarray https://leetcode.com/problems/maximum-product-subarray/?tab=Description

1. https://www.quora.com/How-do-I-solve-maximum-product-subarray-problems
2. Use an example: [2,-3,4,-8,0]
3. Insights:
    What if the array has just positive numbers including zero?
    A solution of this will maintain max_prod[i] where max_prod[i] is the maximum subarray product ending at i. Then max_prod[i+1] = max(max_prod[i] * nums[i+1], nums[i+1]).
    Now how do we change the solution when we allow negative numbers?
    Imagine that we have both max_prod[i] and min_prod[i] i.e. max prod ending at i and min prod ending at i. Now if we have a negative number at nums[i+1] and if min_prod[i] is negative, then the product of the two will be positive and can potentially be largest product. Key point is to maintain both max_prod and min_prod such that at iteration i, they refer to the max and min prod ending at index i -1.
    You have three choices to make at any position in array.

You can get maximum product by multiplying the current element with
    1. maximum product calculated so far. (might work when current
       element is positive).
    2. You can get maximum product by multiplying the current element with
       minimum product calculated so far. (might work when current
       element is negative).
    3. Current element might be a starting position for maximum product sub
       array"""

class Solution2:
    def maxProduct(self, nums):

        max_prod, min_prod, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            y = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod, min_prod = x, y
            ans = max(max_prod, ans)
        return ans

class Solution3:
    def maxProduct(self, nums):

        minlist,maxlist = [nums[0]],[nums[0]]
        for i in range(1,len(nums)):
            minlist.append(min(nums[i],minlist[i-1]*nums[i],maxlist[i-1]*nums[i]))
            maxlist.append(max(nums[i],minlist[i-1]*nums[i],maxlist[i-1]*nums[i]))
        return max(maxlist)



