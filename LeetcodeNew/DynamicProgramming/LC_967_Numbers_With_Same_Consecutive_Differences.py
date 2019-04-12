
"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Note:

1 <= N <= 9
0 <= K <= 9
"""

"""
We initial the current result with all 1-digit numbers,
like cur = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

Each turn, for each x in cur,
we get its last digit y = x % 10.
If y + K < 10, we add x * 10 + y + K to the new list.
If y - K >= 0, we add x * 10 + y - K to the new list.

We repeat this step N - 1 times and return the final result.
"""
class Solution1:
    def numsSameConsecDiff(self, N, K):
        cur = range(10)
        for i in range(N - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + K, x % 10 - K] if x and 0 <= y < 10}
        return list(cur)

"""
题目大意
找出N位数中，所有满足每个数字的所有连续数相减绝对值等于K的数字。比如第一个例子的181就满足|8-1| = |1 - 8| = 7.

解题方法
DFS
明显这是个找出所有符合条件的题目，因此是个搜索题。看了给出的数字的范围只有9位数，大概判断使用DFS不会超时。
因此，我们使用DFS找出所有符合条件的即可。

这里的DFS搜索方法是，我们先确定首位数字是1到9，然后计算以这个数字开头的整数满足条件的有多少。
也就是末位数字 + K <= 9 或者末位数字 + K >= 0两种符合条件，可以继续向后搜索，知道搜索到N==0，
那么搜索结束，把现在的整数放到结果里即可。

题目里面有两个坑：第一，先导0的问题，我在上面搜索的过程中是假设了第一位数字不是0了，那么对于N>=2的时候是满足的，
当N==1的时候直接返回0~9各个数字即可，这点题目没有说清楚，我觉得是不好的。
第二，题目没有专门提到返回的数字不能有重复，我觉得题目应该提醒一下。
"""


class Solution2:
    def numsSameConsecDiff(self, N, K):

        if N == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        for i in range(1, 10):
            self.dfs(res, i, N - 1, K)
        return list(set(res))

    def dfs(self, res, curint, N, K):
        if N == 0:
            res.append(curint)
            return
        last = curint % 10
        if last + K <= 9:
            self.dfs(res, curint * 10 + last + K, N - 1, K)
        if last - K >= 0:
            self.dfs(res, curint * 10 + last - K, N - 1, K)



class Solution3:
    def numsSameConsecDiff(self, N, K):
        ans = {x for x in range(1, 10)}
        for _ in range(N-1):
            ans2 = set()
            for x in ans:
                d = x % 10
                if d - K >= 0:
                    ans2.add(10*x + d-K)
                if d + K <= 9:
                    ans2.add(10*x + d+K)
            ans = ans2

        if N == 1:
            ans.add(0)

        return list(ans)


# 思路 1 - 时间复杂度: O((10-K)^N)- 空间复杂度: O(1)******

class Solution4:
    def numsSameConsecDiff(self, N, K):

        if N == 1:
            return [i for i in range(10)]
        if K == 0:
            return [int(str(i) * N) for i in range(1, 10)]

        self.res = []
        self.dfs('', N, K)
        return [int(i) for i in self.res]

    def dfs(self, path, N, K):
        if len(path) == 0:
            for i in range(1, 10):
                self.dfs(path + str(i), N, K)
            return

        if len(path) == N:
            self.res.append(path)
            return

        if int(path[-1]) + K <= 9:
            self.dfs(path + str(int(path[-1]) + K), N, K)
        if int(path[-1]) - K >= 0:
            self.dfs(path + str(int(path[-1]) - K), N, K)




