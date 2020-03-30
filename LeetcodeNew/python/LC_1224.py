"""
https://leetcode.com/problems/maximum-equal-frequency/discuss/403931/JavaC%2B%2BPython-Easy-to-understand-(compare-counts
"""
"""
Count frequency of the elements
We also need to count the number of elements with that frequency

Explanation
There are 2 cases where we need to update the result:

Case 1:
frequency * (number of elements with that frequency) == length AND i != nums.length - 1
E.g. [1,1,2,2,3]
When the iteration is at index 3, the count will be equal to the length. It should update the result with (length + 1) as it should take an extra element in order to fulfil the condition.

Case 2:
frequency * (number of elements with that frequency) == length - 1
E.g. [1,1,1,2,2,3]
When the iteration is at index 4, the count will be equal to (length - 1). It should update the result with length as it fulfil the condition.

Complexity
Time: O(N) where N is the number of elements
Space: O(N)

"""


import collections

class Solution:
    def maxEqualFreq(self, nums):
        counts = collections.Counter()
        freq = collections.Counter()
        res = 0
        for i, num in enumerate(nums):
            # update counts
            counts[num] += 1
            # update counts with that frequency
            freq[counts[num]] += 1

            prod = freq[counts[num]] * counts[num]
            if prod == i + 1 and i != len(nums) - 1: # case 1
                res = max(res, i + 2)
            elif prod == i: # case 2
                res = max(res, i + 1)
        return res



class Solution2:
    def maxEqualFreq(self, nums) -> int:

        count = [0] * 100001
        freq = [0] * 100001

        n = len(nums)

        for i in range(n):
            count[nums[i]] += 1
            freq[count[nums[i]]] += 1

        for i in range(n - 1, -1, -1):
            if count[nums[i]] * freq[count[nums[i]]] == i:
                return i + 1
            freq[count[nums[i]]] -= 1
            count[nums[i]] -= 1

            if count[nums[i - 1]] * freq[count[nums[i - 1]]] == i:
                return i + 1

        return 1




nums = [2,2,1,1,5,3,3,5]
a = Solution()
print(a.maxEqualFreq(nums))







