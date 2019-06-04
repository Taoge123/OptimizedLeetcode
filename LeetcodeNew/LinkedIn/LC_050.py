# DFS
def permuteUnique(self, nums):
    res, visited = [], [False] * len(nums)
    nums.sort()
    self.dfs(nums, visited, [], res)
    return res


def dfs(self, nums, visited, path, res):
    if len(nums) == len(path):
        res.append(path)
        return
    for i in xrange(len(nums)):
        if not visited[i]:
            if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                continue
            visited[i] = True
            self.dfs(nums, visited, path + [nums[i]], res)
            visited[i] = False
            