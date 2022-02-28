

class SolutionDFS:
    def findDifferentBinaryString(self, nums):
        res = []
        path = ''
        seen = set(nums)
        self.dfs(nums[0], 0, seen, path, res)
        return res[0]

    def dfs(self, s, pos, seen, path, res):

        if len(path) == len(s) and path not in seen:
            res.append(path)

        if pos == len(s):
            return

        self.dfs(s, pos + 1, seen, path + s[pos], res)
        self.dfs(s, pos + 1, seen, path + str(abs(int(s[pos]) - 1)), res)


class Solution: # super fast
    def findDifferentBinaryString(self, nums) -> str:
        self.res = ''
        path = ''
        seen = set(nums)
        self.dfs(nums[0], 0, seen, path)
        return self.res

    def dfs(self, s, pos, seen, path):

        if len(path) == len(s) and path not in seen:
            self.res = path[:]
            return True

        if pos == len(s):
            return False

        for bit in ('1', '0'):
            if self.dfs(s, pos + 1, seen, path + bit):
                return True

        return False




class Solution1:
    def findDifferentBinaryString(self, nums):
        n = len(nums[0])
        # convert str to bit
        arr = [int(num, 2) for num in nums]

        seen = set(arr)
        res = ""
        for i in range(1 << n):
            if i not in seen:
                res = bin(i)[2:]  # convert int to bit, delete '0b'

        m = n - len(res)
        return "0" * m + res  # add zero before it


