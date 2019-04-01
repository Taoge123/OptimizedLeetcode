
"""
Given an array of n integers nums and a target,
find the number of index triplets i, j, k with 0 <= i < j < k < n
that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?
"""


class SolutionCaikehe:
    # O(n*n) time
    def threeSumSmaller(self, nums, target):
        count = 0
        nums.sort()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < target:
                    # if (i,j,k) works, then (i,j,k), (i,j,k-1),...,
                    # (i,j,j+1) all work, totally (k-j) triplets
                    count += k - j
                    j += 1
                else:
                    k -= 1
        return count


class Solution2:
    def threeSumSmaller(self, nums, target):

        nums.sort()
        res = 0
        for i in range(0, len(nums) - 2):
            if 3 * nums[i] >= target:
                return res
            start = i + 1
            end = len(nums) - 1
            while start < end:
                # print nums[i], nums[start], nums[end]
                if nums[i] + nums[start] + nums[end] < target:
                    res += end - start
                    start += 1
                else:
                    end -= 1
        return res



class Solution3:
    def threeSumSmaller(self, nums, target):
        ans = 0
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            prev_ans = ans  # for pruning
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    ans += (k - j)
                    j += 1
                else:
                    k -= 1
            if prev_ans == ans:
                break  # if the ans doesn't change, then larger i won't change ans either
        return ans



class Solution4:

    def threeSumSmaller(self, nums, target):
        nums.sort()
        total, length = 0, len(nums)
        for i in range(length):
            j, k = i + 1, length - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    total += k - j
                    j += 1
                else:
                    k -= 1
        return total

