
"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

"""

"""
解题方法
按照Tag说就是快啊，这个题和306. Additive Number一个一模一样啊，306题是要返回True和False，这个是要求返回具体的一个例子。

因为只要判断能否构成即可，所以不需要res数组保存结果。回溯法仍然是对剩余的数字进行切片，
看该部分切片能否满足条件。剪枝的方法是判断数组是否长度超过3，如果超过那么判断是否满足费布拉奇数列的规则。
不超过3或者已经满足的条件下继续进行回溯切片。最后当所有的字符串被切片完毕，要判断下数组长度是否大于等于3，这是题目要求。

因为题目要求返回任意一个就好了，因此，只要找到一个满足条件的，那么就返回True，再结束循环就好了。所以整个题都是在306的基础上做出来的。

第一遍提交的时候出了个错，第一遍竟然没看出来：

"""

class Solution:
    def splitIntoFibonacci(self, S):

        res = []
        self.dfs(S, [], res)
        return res

    def dfs(self, num_str, path, res):
        if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
            return False
        if not num_str and len(path) >= 3:
            res.extend(path)
            return True
        for i in range(len(num_str)):
            curr = num_str[:i + 1]
            if (curr[0] == '0' and len(curr) != 1) or int(curr) >= 2 ** 31:
                continue
            if self.dfs(num_str[i + 1:], path + [int(curr)], res):
                return True
        return False




