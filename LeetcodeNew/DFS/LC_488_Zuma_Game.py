"""
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

"""

class Solution:
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """
        self.balls = collections.Counter(hand)
        self.ans = float('inf')
        self.dfs(board, 0)
        return self.ans if self.ans < float('inf') else -1

    def dfs(self, board, steps):

        board, N = self.prune(board)

        if not board:
            self.ans = min(self.ans, steps)

        i = 0
        while i < N:
            cur = board[i]
            j = i
            while j < N and board[j] == cur:
                j += 1
            if j - i <= 2 and self.balls[cur] >= 3 - (j - i):
                self.balls[cur] -= 3 - (j - i)
                self.dfs(board[:i] + board[j:], steps + 3 - (j - i))
                self.balls[cur] += 3 - (j - i)
            elif j - i > 2:
                self.dfs(board[:i] + board[j:], steps)
            i = j

    def prune(self, board):
        ans = ''
        N = len(board)
        i = 0
        while i < N:
            j = i
            while j < N and board[j] == board[i]:
                j += 1
            if j - i <= 2:
                ans += board[i:j]
            i = j
        return ans, len(ans)


from collections import Counter


class Solution2:
    def findMinStep(self, board, hand):

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


"""
The basic idea is to do a backtracking DFS choosing the ball 
that will reduce the size of the board each time. 
If there are 3 or more consecutive balls we can immediately choose 
that one knowing that is an optimal step (using zero balls from hand). 
Otherwise first see if we can use one ball (1 step), 
if not try two balls (2 steps).

"""
import collections

class Solution3:
    def findMinStep(self, board, hand):
        hm = collections.defaultdict(int)
        for b in hand:
            hm[b] += 1
        def longestConsecutive(board):
            start,s,e = 0,0,0
            for i in range(len(board)):
                if board[i] != board[start]:
                    start = i
                if i-start > e-s:
                    s,e = start,i
            return (s,e)
        def minStep(board):
            i,n,localMin = 0,len(board),float('inf')
            if n==0: return 0
            start,end = longestConsecutive(board)
            if end-start > 1:
                return minStep(board[:start]+board[end+1:])
            while i < n:
                ball,step = board[i],1 if i < n-1 and board[i]==board[i+1] else 2
                if hm[ball] >= step:
                    hm[ball] -= step
                    ms = minStep(board[:i]+board[i+3-step:])
                    localMin = min(localMin,(step+ms) if ms != -1 else localMin)
                    hm[ball] += step
                i += 3-step
            return localMin if localMin != float('inf') else -1
        return minStep(board)


