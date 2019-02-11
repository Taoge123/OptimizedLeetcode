class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res


class Solution2:
    # DFS
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)



class Solution3:
    def subsetsWithDup(self, nums):
        subsets = []
        nums.sort()
        self.findSubsets(nums, subsets)
        return subsets

    def findSubsets(self, nums, subsets):
        #Linear check
        if nums in subsets:
            return None

        subsets.append(nums)

        for i in range(0, len(nums)):
            temp = self.findSubsets(nums[0:i] + nums[i+1:], subsets)






"""heck if last element of prefix if equal to current
eg [1,2,2]

                            ----- []
              ----- []   
                            -----  [2]
   ----- []  
                            -----  [2] SKIP (current num 2 equal last)
              ------[2]  
                            -----  [2, 2]
	 
[]
                            ------ [1]
              ------[1]
                            ------ [1,2]
   --[1]
                            ------ [1,2] SKIP 	 
              -------[1,2]
                            ------ [1,2,3] 

        """


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.helper(nums)

    def helper(self, nums):
        i = 0
        res = [[]]
        while i < len(nums):
            tmp = []
            for p in res:
                if not p or p[-1] != nums[i]:
                    tmp.append(p)
                tmp.append(p + [nums[i]])
            res = tmp
            i += 1
        return res

#Summary Solution

class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans


