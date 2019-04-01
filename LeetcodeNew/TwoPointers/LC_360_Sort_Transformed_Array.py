
"""
http://www.cnblogs.com/grandyang/p/5595614.html


Given a sorted array of integers nums and integer values a, b and c.
Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
"""

"""
但是题目中的要求让我们在O(n)中实现，那么我们只能另辟蹊径。
其实这道题用到了大量的高中所学的关于抛物线的数学知识，我们知道，
对于一个方程f(x) = ax2 + bx + c 来说，如果a>0，则抛物线开口朝上，那么两端的值比中间的大，
而如果a<0，则抛物线开口朝下，则两端的值比中间的小。而当a=0时，则为直线方法，是单调递增或递减的。
那么我们可以利用这个性质来解题，题目中说明了给定数组nums是有序的，如果不是有序的，我想很难有O(n)的解法。
正因为输入数组是有序的，我们可以根据a来分情况讨论：

当a>0，说明两端的值比中间的值大，那么此时我们从结果res后往前填数，用两个指针分别指向nums数组的开头和结尾，
指向的两个数就是抛物线两端的数，将它们之中较大的数先存入res的末尾，然后指针向中间移，重复比较过程，直到把res都填满。

当a<0，说明两端的值比中间的小，那么我们从res的前面往后填，用两个指针分别指向nums数组的开头和结尾，
指向的两个数就是抛物线两端的数，将它们之中较小的数先存入res的开头，然后指针向中间移，重复比较过程，直到把res都填满。

当a=0，函数是单调递增或递减的，那么从前往后填和从后往前填都可以，我们可以将这种情况和a>0合并。
"""

class Solution1:
    def sortTransformedArray(self, nums, a, b, c):
        nums = [x * x * a + x * b + c for x in nums]
        ret = [0] * len(nums)
        p1, p2 = 0, len(nums) - 1
        i, d = (p1, 1) if a < 0 else (p2, -1)
        while p1 <= p2:
            if nums[p1] * -d > nums[p2] * -d:
                ret[i] = nums[p1]
                p1 += 1
            else:
                ret[i] = nums[p2]
                p2 -= 1
            i += d
        return ret






