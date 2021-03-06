"""
https://leetcode.com/problems/number-of-squareful-arrays/discuss/238550/python-dfs-solution

给定一个非负整数数组A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。

返回A的正方形排列的数目。两个排列A1和A2不同的充要条件是存在某个索引i，使得 A1[i] != A2[i]。

Given an array A of non-negative integers,
the array is squareful if for every pair of adjacent elements,
their sum is a perfect square.

Return the number of permutations of A that are squareful.
Two permutations A1 and A2 differ if and only if there is some index i
such that A1[i] != A2[i].

Example 1:

Input: [1,17,8]
Output: 2
Explanation:
[1,8,17] and [17,8,1] are the valid permutations.
Example 2:

Input: [2,2,2]
Output: 1
"""
"""
给定数字，然后求解符合条件的数字排列。在进行求解的时候，可以将每个数字看成一个节点，
然后转化为求解从任意节点出发，对于其余节点只经过一次的路径个数。
因此可以将此题看做一个哈密顿图问题，解这题的第一种方法是回溯法。

使用递归进行回溯
由于回溯法本质是一种深度优先遍历（dfs），因此在实现的时候可以借助递归的思想进行遍历每个节点，
求解符合条件的路径条数。（虽然递归实现的时间复杂度较高，为n! n!n!，但是由题目中给出的条件：
A.length <=12可知，其时间复杂度最多也只是12！可以接受）

这里有几个问题需要留意一下：

1. 什么样的路径符合条件
   题目中已经出给要求，当（A[i] + 相邻前一个数）是平方数时，这两个节点可以相邻。于是这个条件便可以用作递归条件之一
2. 递归出口如何定义
   当所有节点都遍历完成的时候，意味着遍历结束，跳出递归

"""
"""
Explanation:

1. Count numbers ocuurrence.
2. For each number i, find all possible next number j that i + j is square.
3. Backtracking using dfs.

Time Complexity
    It's O(N^N) if we have N different numbers and any pair sum is square.
    We can easily make case for N = 3 like [51,70,30].

Seems that no hard cases for this problem and int this way it reduces to O(N^2).
"""

import collections

class Solution2:
    def numSquarefulPerms(self, A):
        c, self.res = collections.Counter(A), 0
        can = {i : {j for j in c if (int((i + j) ** 0.5)) ** 2 == i + j} for i in c}
        def dfs(x, idx):
            c[x] -= 1
            if idx == len(A) - 1:
                self.res += 1
            for y in can[x]:
                if c[y]:
                    dfs(y, idx + 1)
            c[x] += 1
        for i in c: dfs(i, 0)
        return self.res


class SolutionLee:
    def numSquarefulPerms(self, A):
        c = collections.Counter(A)
        cand = {i: {j for j in c if int((i + j)**0.5) ** 2 == i + j} for i in c}
        self.res = 0
        def dfs(x, left=len(A) - 1):

            c[x] -= 1
            if left == 0:
                self.res += 1
            for y in cand[x]:
                if c[y]: dfs(y, left - 1)
            c[x] += 1

        for x in c: dfs(x)
        return self.res



"""
题号996在互联网公司是多么吉利的一个数字哈。说说题目，一开始就想到了回溯法，递归求解，
后来看了官方的解答，也是回溯法和动规法，而且是时间复杂度都很高，基本接近穷举法，
这就让人感觉这个题目很无聊了。现在参考官方解答总结一下使用回溯法的解决方案：

（1）可以先统计一下每个数字的出现的次数，并且统计一下，每个数字与其他能组成平方数的数字放到一块，这样做可以节省一定的计算量。

（2）使用回溯法，依次选出一个数字进行深度优先 递归判断。
"""


class Solution3:
    def numSquarefulPerms(self, A):
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:  # 求出那些数字是和x 可以组成平方数的
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:  # 测试是，0.5 加与不加 不影响结果
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:  # 依次选出一个数字进行深度优先 递归判断
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)


if __name__ == '__main__':
    solu = Solution3()
    print(solu.numSquarefulPerms([1, 17, 8]))






