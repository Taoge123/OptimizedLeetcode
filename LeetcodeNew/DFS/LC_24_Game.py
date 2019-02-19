
"""
http://www.cnblogs.com/grandyang/p/8395062.html
https://blog.csdn.net/gangtaolun8493/article/details/78063690

"""
from operator import add, sub, mul, truediv

class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return any(abs(x - 24) < 1e-9 for x in self.solve(nums))
    def solve(self, nums):
        size = len(nums)
        if size == 1:
            return [nums[0]]
        ans = []
        for x in range(size):
            left, n = nums[x], nums[:x] + nums[x+1:]
            for right in self.solve(n):
                ans.append(left + right)
                ans.append(left - right)
                ans.append(left * right)
                if right:
                    ans.append(1.0 * left / right)
        if size >=3:
            for x in range(size):
                for y in range(x + 1, size):
                    left, right = nums[x], nums[y]
                    n = nums[:x] + nums[x+1:y] + nums[y+1:]
                    ans += self.solve([left + right] + n)
                    ans += self.solve([left - right] + n)
                    ans += self.solve([left * right] + n)
                    if right:
                        ans += self.solve([1.0 * left / right] + n)
        return ans



class Solution2:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return abs(nums[0]-24) < 1e-6
        ops = [add, sub, mul, truediv]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                next_nums = [nums[k] for k in range(len(nums)) if i != k != j]
                for op in ops:
                    if ((op is add or op is mul) and j > i) or \
                       (op == truediv and nums[j] == 0):
                        continue
                    next_nums.append(op(nums[i], nums[j]))
                    if self.judgePoint24(next_nums):
                        return True
                    next_nums.pop()
        return False


# Time:  O(n^3 * 4^n) = O(1), n = 4
# Space: O(n^2) = O(1)
from fractions import Fraction
from operator import add, sub, mul, div

class Solution2(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums):
            if len(nums) == 1:
                return nums[0] == 24
            ops = [add, sub, mul, div]
            for i in xrange(len(nums)):
                for j in xrange(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in xrange(len(nums)) if i != k != j]
                    for op in ops:
                        if ((op is add or op is mul) and j > i) or \
                           (op == div and nums[j] == 0):
                            continue
                        next_nums.append(op(nums[i], nums[j]))
                        if dfs(next_nums):
                            return True
                        next_nums.pop()
            return False

        return dfs(map(Fraction, nums))











