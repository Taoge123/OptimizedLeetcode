s
"""
https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90739/Python-DFS-bests-85.-Tips-for-all-DFS-in-matrix-question.

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

"""


"""

The DFS solution is straightforward. Starting from each point, 
and dfs its neighbor if the neighbor is equal or less than itself. 
And maintain two boolean matrix for two oceans, indicating an ocean can reach to that point or not. 
Finally go through all nodes again and see if it can be both reached by two oceans. 
The trick is if a node is already visited, no need to visited again. 
Otherwise it will reach the recursion limits.

This question is very similar to 
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ 

And here are some common tips for this kind of question
1. init a directions var like self.directions = [(1,0),(-1,0),(0,1),(0,-1)] so that when you want to explore from a node, you can just do

for direction in self.directions:
            x, y = i + direction[0], j + direction[1]

2. this is a what I normally do for a dfs helper method for exploring a matrix
"""

#Template
"""
def dfs(self, i, j, matrix, visited, m, n):
  if visited: 
    # return or return a value
  for dir in self.directions:
    x, y = i + direction[0], j + direction[1]
        if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j] (or a condition you want to skip this round):
           continue
        # do something like
        visited[i][j] = True
        # explore the next level like
        self.dfs(x, y, matrix, visited, m, n)"""


class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n - 1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m - 1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result

    def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)



