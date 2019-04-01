
"""
https://leetcode.com/problems/minimum-window-substring/discuss/26808/here-is-a-10-line-template-that-can-solve-most-substring-problems

https://leetcode.com/problems/max-consecutive-ones-ii/discuss/96916/Sliding-window%2B2-pointersO(n)-time-1-passO(1)-space

http://www.cnblogs.com/grandyang/p/6376115.html

5. Longest Palindromic Substring
680. Valid Palindrome II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""
"""
思路：

由于可以允许翻转一次0，所以我们记录两部分内容：zeroLeft表示在需要翻转的0之前的连续1的个数，
zeroRight表示在需要翻转的0之后的连续1的个数。一旦我们遇到一个0，就需要更新zeroLeft和zeroRight了。
最终只要记录下来zeroLeft + zeroRight的最大值即可。注意到这里我们让zeroRight同时包含了需要翻转的0，
这样就可以统一处理只有一个0的情况了。算法的时间复杂度是O(n)，空间复杂度是O(1)。
由于我们不需要对原来出现的数据进行重新存取，所以这个代码也满足了Follow up的要求，可以处理无限长的数据流。
"""

"""
this approach is quite similar to

5. Longest Palindromic Substring
680. Valid Palindrome II
the basic idea is to expand and calculate from center, 

i.e. pre+1+cur/next, practice them in a row for better understanding 😉

"""

"""
store the length of previous and current consecutive 1's (separated by the last 0) as pre and curr , respectively. 

Whenever we get a new number, update these two variables accordingly. 
The consecutive length would be pre + 1 + curr, where the 1 is a zero that got flipped to 1. 
(note that pre is initialized to -1, meaning that we haven't seen any 0 yet)
"""

class Solution1:
    def findMaxConsecutiveOnes(self, nums):
        # previous and current length of consecutive 1
        pre, curr, maxlen = -1, 0, 0
        for n in nums:
            if n == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            maxlen = max(maxlen, pre + 1 + curr)
        return maxlen

class Solution2:
    def findMaxConsecutiveOnes(self, nums):
        zero, mx, j = 0, 0, 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zero += 1
            while zero > 1:
                if nums[j] == 0:
                    zero -= 1
                j += 1
            mx = max(mx, i - j + 1)
        return mx


"""
No need to iterate increment a counter everytime you see a 1. 
Instead, simply remember the index of the second to last 0 seen, 
and update it whenever you see another 0.
"""
class Solution3:
    def findMaxConsecutiveOnes(self, nums):
        prev, curr, max_dist = -1, -1, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_dist = max(max_dist, i - prev - 1)
                prev, curr = curr, i
        return max(len(nums) - prev - 1, max_dist)

