
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        return self.dfs(num, [])

    def dfs(self, num, path):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num and len(path) >= 3:
            return True

        for i in range(len(num)):
            temp = num[:i + 1]
            if temp[0] == '0' and len(temp) != 1:
                continue
            if self.dfs(num[i + 1:], path + [int(temp)]):
                return True
        return False








