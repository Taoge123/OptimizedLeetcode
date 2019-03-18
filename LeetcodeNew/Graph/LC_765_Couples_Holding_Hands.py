
"""
https://leetcode.com/problems/couples-holding-hands/discuss/220967/UnionFind-python
http://www.cnblogs.com/grandyang/p/8716597.html
https://www.itread01.com/content/1544635655.html
https://www.twblogs.net/a/5bb279b52b71770e645de6cb



N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

"""

import collections


class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        pairs = collections.defaultdict(int)

        for i in range(0, len(row), 2):
            pairs[row[i]] = row[i + 1]
            pairs[row[i + 1]] = row[i]

        res = 0
        for pos in range(0, len(row), 2):
            if pairs[pos] != pos + 1:
                left = pairs[pos]
                right = pairs[pos + 1]
                pairs[left] = right
                pairs[right] = left
                res += 1

        return res


"""
用数学归纳法可以比较好的得到为什么用union find 的做法可以解。已知row的长度是2*N

1. N=1 ==> row = [0,1] 或者 row = [1,0] ==> 返回 0

2. N=2 ==> couple_0 = (0,1) couple_1 = (2,3)
   2.1 ==> [(0,1), (2,3)], [(1,0), (2,3)], [(2,3), (1,0)] ==> 返回0
   2.2 ==> 剩下的排列组合情况，只会有一个元素overlap，只需要交换1次就可以了。

3. N=3 ==> couple_0 = (0,1) couple_1 = (2,3) couple_2 = (4,5)
   3.1 最多只能有3个元素overlap，只需要交换2次
   N. 最多只能有N 个元素overlap，交换N-1次
   所以我们只需要通过union find 算法把overlap的元素merge在一起，就能知道需要交换多少次。

"""


class UnionFind:
    def __init__(self, n):  # disjoint union set 模板，请参考花花酱视频
        self.parent = [i for i in range(n)]
        self.counts = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px != py:  # 优化：记录多少次merge操作。 如果不记录counts的话，需要额外的O(N)复杂度来计算
            self.counts += 1
        self.parent[px] = py


class Solution2:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row) // 2
        unionFind = UnionFind(n)

        for i in range(n):
            x = row[2 * i] // 2
            y = row[2 * i + 1] // 2

            if x != y:
                unionFind.merge(x, y)

        return unionFind.counts


"""
Algorithm

We'll construct the graph: adj[node] will be the index of the two nodes 
that this node is adjacent to. After, we'll find all connected components 
(which are also cycles.) If at some couch (node) a person is unvisited, 
we will visit it and repeatedly visit some neighbor until we complete the cycle.
"""
class SolutionOfficial2:
    def minSwapsCouples(self, row):
        N = len(row) / 2

        #couples[x] = [i, j]:
        #x-th couple is at couches i and j
        couples = [[] for _ in range(N)]
        for i, x in enumerate(row):
            couples[x/2].append(i/2)
        #adj[x] = [i, j]
        #x-th couch connected to couches i, j by couples
        adj = [[] for _ in range(N)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)
        #Answer is N minus the number of cycles in "adj"
        ans = N
        for start in range(N):
            if not adj[start]: continue
            ans -= 1
            x, y = start, adj[start].pop()
            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        return ans


"""
Intuition

From guessing, or by the proof in Approach #2, our strategy is to resolve each couch in order.

To resolve a couch, fix the first person and have their partner swap into the second seat if they are not already there.

Algorithm

If a person is number x, their partner is x ^ 1, where ^ is the bitwise XOR operator.

For each first person x = row[i] on a couch who is unpartnered, 
let's find their partner at row[j] and have them swap seats with row[i+1].
"""
class Solution4:
    def minSwapsCouples(self, row):
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i+1] == x^1: continue
            ans += 1
            for j in range(i+1, len(row)):
                if row[j] == x^1:
                    row[i+1], row[j] = row[j], row[i+1]
                    break
        return ans





