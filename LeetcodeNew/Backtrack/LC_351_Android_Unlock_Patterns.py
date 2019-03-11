"""

Given an Android 3x3 key lock screen and two integers m and n,
where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen,
which consist of minimum of m keys and maximum n keys.



Rules for a valid pattern:

Each pattern must connect at least m keys and at most n keys.
All the keys must be distinct.
If the line connecting two consecutive keys in the pattern
passes through any other keys, the other keys must have previously selected in the pattern.
No jumps through non selected key is allowed.
The order of keys used matters.

Explanation:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Invalid move: 4 - 1 - 3 - 6
Line 1 - 3 passes through key 2 which had not been selected in the pattern.

Invalid move: 4 - 1 - 9 - 2
Line 1 - 9 passes through key 5 which had not been selected in the pattern.

Valid move: 2 - 4 - 1 - 3 - 6
Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

Valid move: 6 - 5 - 4 - 1 - 9 - 2
Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.



Example:

Input: m = 1, n = 1
Output: 9


"""



class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        skip = {}

        skip[(1, 7)] = 4
        skip[(1, 3)] = 2
        skip[(1, 9)] = 5
        skip[(2, 8)] = 5
        skip[(3, 7)] = 5
        skip[(3, 9)] = 6
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        self.res = 0

        def bfs(used, last):
            if len(used) >= m:
                self.res += 1
            if len(used) == n:
                return
            for j in range(1, 10):
                if j not in used:  # if j is not used
                    # Sort the vertices of the edge to search in skip
                    edge = (min(last, j), max(last, j))
                    if edge not in skip or skip[edge] in used:
                        bfs(used + [j], j)

        for i in range(1, 10):
            bfs([i], i)
        return self.res



"""
Create a dictionary to store all valid next movements according to the current number. 
For example: 2:[1,3,4,6,7,9]. If the current number is 2, 
and 1,3,4,5,6,7,9 are all valid movements.
Create a dictionary to store might-be-valid movements (key, value pair). 
For example: 2:{5:8}. The key-value pair indicates that if the previous movements 
include a key, then the value is a valid movement. If the current number is 2, and 5 
is already in the previous movements, then 8 is the valid movement for the next move.
"""


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        self.res = 0
        self.inDirectValid = {1: {2: 3, 4: 7, 5: 9}, 2: {5: 8}, 3: {2: 1, 5: 7, 6: 9}, 4: {5: 6}, 5: {}, 6: {5: 4},
                              7: {4: 1, 5: 3, 8: 9},
                              8: {5: 2}, 9: {8: 7, 5: 1, 6: 3}}

        self.directValid = {1: [2, 4, 5, 6, 8], 2: [1, 3, 4, 5, 6, 7, 9], 3: [2, 4, 5, 8, 6],
                            4: [1, 2, 3, 5, 7, 8, 9], 5: [1, 2, 3, 4, 6, 7, 8, 9], 6: [1, 2, 3, 5, 7, 8, 9],
                            7: [2, 4, 5, 6, 8], 8: [1, 4, 5, 7, 3, 6, 9], 9: [2, 4, 5, 6, 8]}

        self.helper([] + [1], m, n)
        self.helper([] + [2], m, n)
        self.res *= 4
        self.helper([] + [5], m, n)

        return self.res

    def helper(self, path, m, n):
        if m <= len(path) <= n:
            self.res += 1
        if len(path) >= n:
            return
        # calculate the valid next steps

        cur = path[-1]
        preMovements = path[:-1]
        dictTemp = self.inDirectValid[cur]
        validMovement = self.directValid[cur][:]

        for move in preMovements:
            if move in dictTemp:
                validMovement.append(dictTemp[move])
        for val in list(set(validMovement) - set(preMovements)):
            self.helper(path + [val], m, n)



class Solution2:
    def findpattern(self, x, table, current, m, n):

        table[x] = True

        if current >= m:
            self.result += 1

        for i in range(1, 10):
            if table[i]:
                continue
            if not table[self.able[x][i]]:
                continue

            if current == n - 1:
                self.result += 1
            else:
                self.findpattern(i, table, current + 1, m, n)

        table[x] = False

    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        self.result = 0

        self.able = [[0 for j in range(10)] for i in range(10)]
        self.able[1][3] = self.able[3][1] = 2
        self.able[1][7] = self.able[7][1] = 4
        self.able[9][3] = self.able[3][9] = 6
        self.able[7][9] = self.able[9][7] = 8
        self.able[1][9] = self.able[9][1] = 5
        self.able[7][3] = self.able[3][7] = 5
        self.able[2][8] = self.able[8][2] = 5
        self.able[4][6] = self.able[6][4] = 5

        table = [False for i in range(10)]
        table[0] = True
        self.findpattern(1, table, 1, m, n)
        self.findpattern(2, table, 1, m, n)

        self.result *= 4

        self.findpattern(5, table, 1, m, n)

        return self.result



"""
1. Since we just need to return an integer, I use 0-8 instead of 1-9 for simplicity.
2. Cross indicates the numbers we can't directly reach (from the index)
3. We can only cross those number when those number has already included, 
we can calculate the number between two numbers by (n1 + n2) / 2, e.g. (2 + 8) / 2 = 5, 
so 5 is the number between 2 and 8.

4. 1, 3, 7, 9 and 2, 4, 6, 8 are exactly the same, 
so we just calculate one each and multiply by 4.

"""
class Solution(object):
    def numberOfPatterns(self, m, n):
        cross = ((2, 6, 8), (7,), (0, 6, 8), (5,), (), (3,), (0, 2, 8), (1,), (0, 2, 6))
        def helper(curr):
            if len(curr) > n: return 0
            total = 1 if m <= len(curr) <= n else 0
            for i in xrange(9):
                if i not in curr and (i not in cross[curr[-1]] or i + curr[-1] >> 1 in curr):
                    total += helper(curr + (i,))
            return total
        return helper((0,)) * 4 + helper((1,)) * 4 + helper((4,))




class Solution(object):
    def numberOfPatterns(self, m, n):
        touchedMove = {
            (1,3):2, (1,7):4, (1,9):5,
            (2,8):5,
            (3,1):2, (3,7):5, (3,9):6,
            (4,6):5,
            (6,4):5,
            (7,1):4, (7,3):5, (7,9):8,
            (8,2):5,
            (9,1):5, (9,3):6, (9,7):8
        }

        self.count = 0
        def moveNext(prev, toChoose, remain):
            if remain == 0:
                self.count += 1
                return

            for i in toChoose:
                if ((prev, i) not in touchedMove) or (touchedMove[(prev, i)] not in toChoose):
                    moveNext(i, toChoose-set([i]), remain-1)

        for i in range(m, n+1):
            moveNext(0, set(range(1,10)), i)

        return self.count