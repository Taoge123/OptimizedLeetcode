

"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

Examples:

Input: "WRRBBW", "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW

Input: "WWRRBBWW", "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty

Input:"G", "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty

Input: "RBYYBBRRB", "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty

Note:
You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
The number of balls on the table won't exceed 20, and the string represents these balls is called "board" in the input.
The number of balls in your hand won't exceed 5, and the string represents these balls is called "hand" in the input.
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""

import collections

class SolutionFast:
    def findMinStep(self, board, hand):
        return self.dfs(board, collections.Counter(hand))

    def dfs(self, board, counter):
        if not board:
            return 0
        res, i = float("inf"), 0
        while i < len(board):
            j = i + 1
            while j < len(board) and board[i] == board[j]:
                j += 1
            need = 3 - (j - i)
            if counter[board[i]] >= need:
                need = 0 if need < 0 else need
                counter[board[i]] -= need
                temp = self.dfs(board[:i] + board[j:], counter)
                if temp >= 0:
                    res = min(res, temp + need)
                counter[board[i]] += need
            i = j
        return res if res != float("inf") else -1




class SolutionFast2:
    def findMinStep(self, board: str, hand: str) -> int:
        count = collections.Counter(hand)
        self.res = len(hand) + 1
        self.dfs(list(board + '#'), count, hand)
        return -1 if self.res > len(hand) else self.res

    def reduce(self, balls):
        i = 0
        for j, ball in enumerate(balls):
            if ball == balls[i]:
                continue
            if j - i >= 3:
                return self.reduce(balls[0:i] + balls[j:])
            else:
                i = j
        return balls

    def dfs(self, board, count, hand):
        board = self.reduce(board)
        if board == ['#']:
            self.res = min(self.res, len(hand) - sum(list(count.values())))
        i = 0
        for j in range(len(board)):
            if board[i] == board[j]:
                continue
            need = 3 - (j - i)
            if count[board[i]] >= need:
                count[board[i]] -= need
                self.dfs(board[0:i] + board[j:], count, hand)
                count[board[i]] += need
            i = j



