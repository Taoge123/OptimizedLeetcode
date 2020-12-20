"""
https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419992/easy-peasy-python-solution-with-explanation
Straightforward Solution: similar to the idea in the solution for 828. Unique Letter String
"""



"""
Have you read this? 992. Subarrays with K Different Integers
Exactly K times = at most K times - at most K - 1 times
"""


class Solution:
    def numberOfSubarrays(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k - 1)

    def atMost(self, nums, k):
        res = left = 0
        for right in range(len(nums)):
            k -= nums[right] % 2
            while k < 0:
                k += nums[left] % 2
                left += 1
            res += right - left + 1
        return res


"""
Actually it's same as three pointers.
Though we use count to count the number of even numebers.
"""


class Solution2:
    def numberOfSubarrays(self, nums, k):
        left = count = res = 0

        for right in range(len(nums)):
            if nums[right] & 1:
                k -= 1
                count = 0

            while k == 0:
                k += nums[left] & 1
                left += 1
                count += 1
            res += count

        return res




class Solution3:
    def numberOfSubarrays(self, nums, k: int) -> int:
        table = {0: 1}
        count = 0
        res = 0

        for i, num in enumerate(nums):
            if num % 2 == 1:
                count += 1

            if count - k in table:
                res += table[count - k]

            table[count] = table.get(count, 0) + 1

        return res

