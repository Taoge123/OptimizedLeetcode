"""

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

"""
import math

class Solution:

    def getFactors(self, n):
        res = []
        self.dfs(self.factors(n)[1:-1], n, 0, [], res)
        return res

    def dfs(self, nums, n, index, path, res):
        tmp = reduce(lambda x, y: x * y, path, 1)
        if tmp > n:
            return  # backtracking
        if tmp == n and path:
            res.append(path)
            return  # backtracking
        for i in range(index, len(nums)):
            self.dfs(nums, n, i, path + [nums[i]], res)

    def factors(self, n):
        res = []
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
        return res



class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1: return []
        res = []
        def dfs(path=[], rest=2, target=n):
            if len(path)>0:
                res.append(path+[target])
            for i in range(rest, int(math.sqrt(target))+1): # i <= target//i, i.e., i <= sqrt(target)
                if target%i==0:
                    dfs(path+[i], i, target//i)
        dfs()
        return res




class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.output=[]
        self.dfs(n,2,[])
        return self.output


    def dfs(self,num,f,curf):
        if len(curf)>0 and num>=f:
            self.output.append(curf+[num])
        for i in range(f,int(math.sqrt(num))+1):
            if num%i==0:
                self.dfs(num/i,i,curf+[i])


class Solution:
    def getFactors(self, n):
        ret = []
        self.dfs(n, [], ret)
        return ret

    def dfs(self, left, cur, ret):
        if cur and cur == sorted(cur):
            ret.append(cur + [left])
        for i in range(2, int(left ** 0.5) + 1):
            if left % i == 0:
                cur.append(i)
                self.dfs(left // i, cur, ret)
                cur.pop()



