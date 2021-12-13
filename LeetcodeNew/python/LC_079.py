"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""



class SolutionTony:
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, visited):
                    return True
        return False

    def dfs(self, board, i, j, word, visited):
        m, n = len(board), len(board[0])
        if not word:
            return True
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
            return False
        if board[i][j] != word[0]:
            return False

        visited[i][j] = True
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            if self.dfs(board, x, y, word[1:], visited):
                return True
        visited[i][j] = False



class Solution:
    def exist(self, board, word):

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.search(board, word, i, j, m, n):
                    return True
        return False

    def search(self, board, word, i, j, m, n):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        result = self.search(board, word[1:], i + 1, j, m, n) \
                 or self.search(board, word[1:], i - 1, j, m, n) \
                 or self.search(board, word[1:], i, j + 1, m, n) \
                 or self.search(board, word[1:], i, j - 1, m, n)
        board[i][j] = temp
        return result






#
# board =[
#           ['A','B','C','E'],
#           ['S','F','C','S'],
#           ['A','D','E','E']
#         ]
# word = "ABCCED"
#

board, word = ['a'], 'a'
a = SolutionTony()
print(a.exist(board, word))
