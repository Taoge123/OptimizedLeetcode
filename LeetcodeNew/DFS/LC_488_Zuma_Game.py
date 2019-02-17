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


"""
When we come to a new cell, we turn left. 
If we try to go and turn right 3 times, 
we have covered everything in front of us and we should backtrack. 
If we can go to a direction, since we are facing backward for backtracking, 
we should turn left instead of right (if we didn't go, 
we would still face the direction, not its reverse). 
Also, when we are done with a cell, we should come back from it. 
Here is a minimalist code to solve the problem.
"""

DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # facing up, turning right as index increases


def dfs(robot, coord, dindex, visited):
    visited.add(coord)
    robot.clean()
    last_move = True
    for di in [3, 0, 1, 2]:
        robot.turnLeft() if last_move else robot.turnRight()
        d = DIRS[(dindex + di) % 4]
        new_c = (coord[0] + d[0], coord[1] + d[1])

        if new_c not in visited and robot.move():
            dfs(robot, new_c, (dindex + di) % 4, visited)
            robot.move()  # come back
            last_move = True
        else:
            last_move = False


class Solution5:
    def cleanRoom(self, robot):
        DIRS = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # facing up, turning right as index increases
        visited = set()

        def dfs(robot, coord, dindex):
            visited.add(coord)
            robot.clean()
            last_move = True

            for di in [3, 0, 1, 2]:
                if last_move:  # 固定先左后右
                    robot.turnLeft()
                else:
                    robot.turnRight()
                d = DIRS[(dindex + di) % 4]  # 調整方向
                new_c = (coord[0] + d[0], coord[1] + d[1])  # 下一步的位置

                if new_c not in visited and robot.move():  # 看一看可不可以前進
                    dfs(robot, new_c, (dindex + di) % 4)  # 前進
                    robot.move()  # come back                #精華，有前進就必須有相應的後退!!!原路返回
                    last_move = True  # 下一步繼續嘗試向左轉
                else:  # 某個點訪問過了或者不可訪問
                    last_move = False  # 下一步向右轉

        dfs(robot, (0, 0), 0)

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        dfs(robot, (0, 0), 0, set())


# left, up, right, down
DIR = ((0, -1), (-1, 0), (0, 1), (1, 0))


class Solution6:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # assume we start at (0, 0) the origin
        self.dfs(robot, (0, 0), set(), 1)

    def dfs(self, robot, curr_pos, visited, facing_direction):
        robot.clean()
        visited.add(curr_pos)

        for i in range(4):
            robot.turnLeft()
            # for i in [0, 3], i+1 means how many times we have turned left
            # (facing_direction - (i + 1)) % 4 therefore, is our new facing direction
            new_direction = (facing_direction - i - 1) % 4
            new_pos = (curr_pos[0] + DIR[new_direction][0], curr_pos[1] + DIR[new_direction][1])
            if new_pos not in visited and robot.move():
                self.dfs(robot=robot,
                         curr_pos=new_pos,
                         visited=visited,
                         facing_direction=new_direction)
                # turn around
                robot.turnLeft()
                robot.turnLeft()
                # move back
                robot.move()
                # face the previous direction, such that we can continue turning left
                robot.turnLeft()
                robot.turnLeft()


