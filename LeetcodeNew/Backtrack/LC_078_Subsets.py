

"""
Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""

class Solution:
    # DFS recursively
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    # Bit Manipulation
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    # Iteratively
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res


class Solution2:
    class Solution(object):
        def subsets(self, nums):
            nums.sort()
            result = [[]]
            for num in nums:
                result += [i + [num] for i in result]
            return result



class Solution3:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
    	if S == []:
    		return []
        S.sort() #sort the array to avoid descending list of int
        res=[[]]
        for element in S:
        	temp = []
        	for ans in res:
        		 #append the new int to each existing list
        		temp.append(ans+[element])
        	res += temp
        return res


class Solution4:
    def dfs(self, nums, path, res):
        if len(nums) == 0:
            return
        for i, n in enumerate(nums):
            res.append(path + [n])
            self.dfs(nums[i+1:], path + [n], res)
    def subsets(self, nums):
        res = [[]]
        self.dfs(nums, [], res)
        return res

