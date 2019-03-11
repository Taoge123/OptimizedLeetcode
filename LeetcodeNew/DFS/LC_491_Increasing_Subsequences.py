"""

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]



This is a back tracking solution, similar to find the subset.
The tricky part is to use a dictionary to check whether the number has been used or not.

1. 如果你看出来这道题和最长上升子序列是一模一样的话那么答案做出来也就不难了，这也是为什么我把这道题归入dp类的原因
2. 我们可以先思考一下LIS问题是怎么处理的，我们使用dp[i]表示前i个数字组成的序列中以nums[i]结尾的最长上升子序列的长度，
dp[i] = max([dp[j]+1 for j in range(i) if nums[j] < nums[i]])
3. 根据这个思路我们可以想到这道题其实也可以用一样的方法，我们使用一个字典d，d[i]表示以nums[i]结尾的上升子序列，初始化所有的d[i] = [[nums[i]]]
4. 则可获得递推式 d[i].append(l+nums[i]) for j in range(i) if nums[j] <= nums[i] for l in d[j]
5. 当然严格来说上式不能算是递推式，我们直接用给出的具体实例来看一下是怎么运作的，初始化d = {0:[[4]],1:[[6]],2:[[7]],3:[[7]]}，
我们从1开始分析，nums[1] > nums[0]，所以d[1] = [[6],[4,6]]，依次类推d[2] = [[4,7],[6,7],[4,6,7]]，d[3] = …
"""


class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 初始化字典
        d = {i: [[nums[i]]] for i in range(len(nums))}
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for l in d[j]:
                        d[i].append(l + [nums[i]])

        s = set()
        res = []
        for i in range(len(nums)):
            for l in d[i]:
                # 因为字典中本身存在长度为1的list，需要我们排除
                if len(l) < 2: continue
                if tuple(l) in s: continue
                s.add(tuple(l))
                res.append(l)
        return res



import itertools
class Solution:
    def findSubsequences(self, nums):
        ret = []
        for i in range(2, len(nums) + 1):
            ret.extend(set(itertools.combinations(nums, i)))
        return [x for x in ret if self.isIncreasing(x)]

    def isIncreasing(self, l):
        for i in range(1, len(l)):
            if l[i - 1] > l[i]:
                return False
        return True


class Solution2(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsets(nums, 0, [], res)
        return res

    def subsets(self, nums, index, temp, res):
        if len(nums) >= index and len(temp) >= 2:
            res.append(temp[:])
        used = {}
        for i in range(index, len(nums)):
            if len(temp) > 0 and temp[-1] > nums[i]: continue
            if nums[i] in used: continue
            used[nums[i]] = True
            temp.append(nums[i])
            self.subsets(nums, i + 1, temp, res)
            temp.pop()

"""
A backtracking solution to find all possible cases.
Use hashset to remove the duplicates.
Because list is not hashable, so I use tuple to save the current elements in each recursion.
The time complexity is exponential for sure, but the code is relatively short.
"""


class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hashset = set()
        prev = -101  # numbers are in the range of [-100,100]
        self.backTrack(nums, 0, (), prev, hashset)
        return list(hashset)

    def backTrack(self, nums, index, currTuple, prev, hashset):
        # print currList
        if len(currTuple) > 1: hashset.add(currTuple)
        if index == len(nums): return
        for i in range(index, len(nums)):
            if nums[i] >= prev:
                self.backTrack(nums, i + 1, currTuple + (nums[i],), nums[i], hashset)



