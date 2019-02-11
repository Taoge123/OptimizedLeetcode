
class Solution:
    def partition(self, s):
        ret = []
        self.dfs(s, 0, [], ret)
        return ret

    def dfs(self, s, index, cur, ret):
        if index >= len(s):
            ret.append(cur[::])
            return
        for i in range(index, len(s)):
            temp = s[index:i + 1]
            cur.append(temp)
            if temp == temp[::-1]:
                self.dfs(s, i + 1, cur, ret)
            cur.pop()


#Solution 2 --- DFS + DP

"""
The DFS (recursive) part: If aa | b the first partition has to be palindrom, 
for example ab | bb is not valid, because ab is not palindrom, 
so this position cannot be a solution. 
So we have a recursive relation [palindrom] | [rest of the string] , 
then we do exactly the same for [rest of the string]. 
Here the return value should be all valid solutions for the substring (starts from start).
The DP part: because we need to check whether a substring is palindrom over and over again, 
and the results are overlaping, so we use a matrix to store the results and reuse them if needed.

"""


class Solution:


    def partitionAfter(self, s, start, valid):
        result = []
        if start == len(s):
            result.append([])
            return result
        for i in range(start, len(s)):
            if s[i] == s[start] and (i == start or i == start + 1 or valid[start + 1][i - 1]):
                valid[start][i] = True
                for sp in self.partitionAfter(s, i + 1, valid):
                    result.append([s[start:i + 1]] + sp)
        return result


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        sl = len(s)
        valid = [x[:] for x in [[False] * sl] * sl]
        return self.partitionAfter(s, 0, valid)


class Solution:
    def partition(self, s):
        def backtrack(start, end, tmp):
            if start == end:
                ans.append(tmp[:])
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
        ans = []
        backtrack(0, len(s), [])
        return ans


