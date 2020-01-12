

"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


class Solution:
    def findCircleNum(self, M):
        n = len(M)
        parents = list(range(n))
        for i in range(n):
            for j in range(len(M[i])):
                if M[i][j]:
                    self.union(parents, i, j)
        res = set()
        for i in range(n):
            res.add(self.find(parents, i))
        return len(res)

    def find(self, parents, x):
        if x != parents[x]:
            parents[x] = self.find(parents, parents[x])
        return parents[x]

    def union(self, parents, x, y):
        parents[self.find(parents, x)] = self.find(parents, y)




class Solution2:
    def findCircleNum(self, M):
        N = len(M)
        visited = set()
        res = 0
        for i in range(N):
            if i not in visited:
                self.dfs(i, M, visited)
                res += 1
        return res

    def dfs(self, node, M, visited):
        for i, val in enumerate(M[node]):
            if val and i not in visited:
                visited.add(i)
                self.dfs(i, M, visited)



M = [[1,1,0],
     [1,1,0],
     [0,0,1]]

a = Solution()
print(a.findCircleNum(M))




