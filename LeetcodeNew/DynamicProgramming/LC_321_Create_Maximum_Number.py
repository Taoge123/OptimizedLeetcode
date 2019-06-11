
"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]
"""
"""
To create the max number from num1 and nums2 with k elements, 
we assume the final result combined by i numbers (denotes as left) from num1 and j numbers (denotes as right) from nums2, where i+j==k.

Obviously, left and right must be the maximum possible number in num1 and num2 respectively. 
i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].

The final result is the maximum possible merge of all left and right.

So there're 3 steps:

iterate i from 0 to k.
find max number from num1, num2 by select i , k-i numbers, denotes as left, right
find max merge of left, right
function maxSingleNumber select i elements from num1 that is maximum. 
The idea find the max number one by one. i.e. assume nums [6,5,7,1,4,2], selects = 3.
1st digit: find max digit in [6,5,7,1], the last two digits [4, 2] can not be selected at this moment.
2nd digits: find max digit in [1,4], since we have already selects 7, 
we should consider elements after it, also, we should leave one element out.
3rd digits: only one left [2], we select it. and function output [7,4,2]

function mergeMax find the maximum combination of left, and right."""

class Solution1:
    def maxNumber(self, nums1, nums2, k):
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret


    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n : return ret
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret


"""
his problem could be divided into 2 sub-problems:

function getMax(nums, t):
get t numbers from list nums to form one single maximized sub-list, with relative orders preserved

function merge(nums1, nums2):
merge nums1 and nums2 to form one single maximized list, with relative orders preserved

The final result could be solved by enumerate the length of sub-list nums1 and nums2, and record the max merged list.
解题思路：
问题可以转化为这样的两个子问题：

1. 从数组nums中挑选出t个数，在保持元素相对顺序不变的情况下，使得选出的子数组最大化。

2. 在保持元素相对顺序不变的前提下，将数组nums1与数组nums2合并，使合并后的数组最大化。
枚举nums1子数组与nums2子数组的长度len1, len2，在满足长度之和len1+len2等于k的前提下，分别求解最大子数组，并进行合并。

然后从合并得到的子数组中取最大数组即为所求。

子问题1的求解：

参考[LeetCode]Remove Duplicate Letters的思路，利用栈保存最大值子数组

时间复杂度为O(n)，其中n为数组的长度。

子问题2的求解：

两数组的合并可以类比归并排序中的merge操作，只不过在选择两数组中较大的元素时，需要对数组剩余部分的元素进行比较，详见代码。


Python Code:
"""

class Solution2:
    def maxNumber(self, nums1, nums2, k):
        def getMax(nums, t):
            ans = []
            size = len(nums)
            for x in range(size):
                while ans and len(ans) + size - x > t and ans[-1] < nums[x]:
                    ans.pop()
                if len(ans) < t:
                    ans += nums[x],
            return ans

        def merge(nums1, nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans

        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            res = max(tmp, res)
        return res










