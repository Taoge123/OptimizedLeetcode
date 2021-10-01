"""
416. Partition Equal Subset Sum
698. Partition to K Equal Sum Subsets - identical - 473. Matchsticks to Square
996. Number of Squareful Arrays

can be solved by using bitmask
"""



class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        target = sum(nums)
        if target % k:
            return False
        target //= k
        table = [0] * k
        nums = sorted(nums, reverse=True)
        return self.dfs(nums, table, 0, k, target)

    def dfs(self, nums, table, index, k, target):
        if index == len(nums):
            for i in range(1, len(table)):
                if table[i] != table[i - 1]:
                    return False
            return True

        for i in range(k):
            if table[i] + nums[index] > target:
                continue
            table[i] += nums[index]
            if self.dfs(nums, table, index + 1, k, target):
                return True
            table[i] -= nums[index]

        return False




