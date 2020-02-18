

"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.



Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.


Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

#Basic idea is
"""
[a1, a2, a3, ......, ak] % k
[a1, a2, a3, ......, ak, ak+1, ...., an] % k
then we will know that
[ak+1, ..., an] also mod k
"""

class SolutionBetter:
    def checkSubarraySum(self, nums, k: int) -> bool:
        summ = 0
        table = {}
        table[0] = -1
        for i in range(len(nums)):
            summ += nums[i]
            if k != 0:
                summ = summ % k

            if summ in table:
                if i - table[summ] > 1:
                    return True
            else:
                table[summ] = i

        return False



class SolutionNaive:
    def checkSubarraySum(self, nums, k: int) -> bool:

        for i in range(len(nums)):
            summ = nums[i]
            for j in range(i + 1, len(nums)):
                summ += nums[j]
                if summ == k:
                    return True
                if k != 0 and summ % k == 0:
                    return True

        return False




class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:

        table = {0 : -1}
        summ = 0
        for i, num in enumerate(nums):
            summ = (summ + num) % k if k else summ + num
            if summ not in table:
                table[summ] = i
            else:
                if i - table[summ] >= 2:
                    return True
        return False



nums = [23, 2, 6, 4, 7]
k=6
a = Solution()
print(a.checkSubarraySum(nums, k))


