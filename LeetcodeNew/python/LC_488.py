

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

from collections import Counter


class Solution:
    def findMinStep(self, board: 'str', hand: 'str') -> 'int':

        self.ans = 2147483647
        self.initlenofhand = len(hand)
        dic = Counter(hand)

        def helper(board, n, dic):

            if not board:
                self.ans = min(self.ans, self.initlenofhand - n)
                return

            for i, char in enumerate(board):
                if i > 0 and char == board[i - 1]:
                    continue
                j = i
                while j < len(board) and board[j] == char:
                    j += 1
                if j - i >= 3:
                    helper(board[:i] + board[j:], n, dic)
                elif j - i == 2 and dic[char] > 0:
                    dic[char] -= 1
                    helper(board[:i] + board[j:], n - 1, dic)
                    dic[char] += 1
                elif dic[char] > 0:
                    dic[char] -= 1
                    helper(board[:i] + char + board[i:], n - 1, dic)
                    dic[char] += 1

        helper(board, len(hand), dic)
        return self.ans if self.ans != 2147483647 else -1



