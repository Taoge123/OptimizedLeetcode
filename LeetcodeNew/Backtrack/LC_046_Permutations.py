# DFS
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res


def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


def permuteIterative(self, nums):
    ans = [nums]
    for i in range(1, len(nums)):
        m = len(ans)
        for k in range(m):
            for j in range(i):
                ans.append(ans[k][:])
                ans[-1][j], ans[-1][i] = ans[-1][i], ans[-1][j]
    return ans


class Solution:
    def permute(self, nums):
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, temp):
        if len(nums) == len(temp):
            self.res.append(temp[:])
            return

        for i in range(len(nums)):
            if nums[i] in temp: continue
            temp.append(nums[i])
            self.dfs(nums, temp)
            temp.pop()


#####
""" Start: [[1],[2],[3]]
    First:  [12][13][21][23][31][33]
    Fist:[123][132]

        1        2          3
     /   \      /  \       / \
    12   13    21  23     31  32
    |     |     |   |      |   |
   123   132   213  231   312 321                 

"""


#Solution 2 -- BFS

"""
先把起始状态的queue存好: [[1],[2],[3]]

while这一层检查我们queue里面是否有比input nums长度小的单位，
如果有的话，咱还有针对这个queue里面的元素进行增值。

for这一层把pop()出来的数组temp，进行去重比对，
如果发现nums里面的元素没有出现在temp，代表着这是unique的，
我们这个数组的的copy temp[:]加上当前的值，放回queue中。
"""

from collections import deque
class Solution:
    def permute(self, nums):
        q = deque()
        for num in nums:
            q.append([num])

        while len(min(q,key=len)) < len(nums):
            temp = q.popleft()
            for num in nums:
                if num in temp: continue
                q.append(temp[:] + [num])
        return list(q)


#BFS (Acting like using Deque)
from collections import deque
class Solution:
    def permute(self, nums):
        q = [[num] for num in nums]
        while len(min(q,key=len)) < len(nums):
            temp = q.pop(0)
            for num in nums:
                if num in temp: continue
                q.append(temp[:] + [num])
        return q


#SUmmary Solution
class Sulution:
    def permute(self, nums):
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0, len(nums))
        return ans



