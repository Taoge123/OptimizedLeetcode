"""

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2,
one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.

According to https://en.wikipedia.org/wiki/Partition_problem,
the partition problem (or number partitioning)
is the task of deciding whether a given multiset S of positive integers
can be partitioned into two subsets S1 and S2
such that the sum of the numbers in S1 equals the sum of the numbers in S2.
The partition problem is NP-complete.
When I trying to think how to apply dynamic programming solution of above problem
to this one (difference is divid S into 4 subsets),
I took another look at the constraints of the problem:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.

Sounds like the input will not be very large...
Then why not just do DFS? In fact, DFS solution passed judges.


"""


class Solution(object):
    def makesquare(self, nums):
        if not nums:
            return False
        sumn = sum(nums)
        nums.sort(reverse=True)
        if sumn % 4:
            return False
        return self.dfs(nums, [0, 0, 0, 0], 0, sumn / 4)

    def dfs(self, nums, t, pos, target):
        if pos == len(nums):
            if t[0] == t[1] == t[2]:
                return True
            return False
        for i in range(4):
            if t[i] + nums[pos] > target:
                continue
            t[i] += nums[pos]
            if self.dfs(nums, t, pos + 1, target):
                return True
            t[i] -= nums[pos]
        return False


class Solution2(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, pos, target):
            if pos == len(nums): return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target): return True
                    target[i] += nums[pos]
            return False
        if len(nums) < 4 : return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % 4 != 0: return False
        target = [numSum/4] * 4;
        return dfs(nums,0, target)


