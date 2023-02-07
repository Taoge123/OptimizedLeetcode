
"""
https://leetcode.com/problems/remove-k-digits/solutions/401228/short-java-solution-using-recursion/

1673. Find the Most Competitive Subsequence

解决原题的直观思路是寻找一个尽可能小的递增序列，但要满足位数的要求。

这是栈的典型应用。利用栈维护一个递增序列。当遍历的元素小于栈顶元素时，就不断退栈直至 Stack.top()<num[i]，这样继续加入元素后仍然是一个递增序列。

需要注意的几点：

需要一个计数器count来记录退栈的数目。只有当count<k时，才进行退栈操作（即模拟删除）。
都把所有元素都遍历结束后，如果发现仍然count<k，那么就把Stack末尾的弹出，直至count==k
需要去除结果里的前导零。

"""

import functools

class SolutionDFS:
    def removeKdigits(self, num, k):
        n = len(num)
        def remove_leading_zero(num):
            i = 0
            while i < len(num) and num[i] == '0':
                i += 1
            if i == len(num):
                return '0'
            return num[i:]

        @functools.lru_cache(None)
        def dfs(num, k):
            if k == n:
                return '0'
            if k == 0:
                return remove_leading_zero(num)

            i = 0
            while i < len(num) - 1 and num[i] <= num[i + 1]:
                i += 1

            return dfs(num[:i] + num[i + 1:], k - 1)
        return dfs(num, k)




class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        if k >= len(num):
            return "0"

        for item in num:
            # we will pop when node decrease
            while stack and k and stack[-1] > item:
                stack.pop()
                k -= 1
            stack.append(item)
        # if we there are k remains, we continue to pop
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))


class SolutionToBeFixed:
    def removeKdigits(self, num: str, k: int) -> str:
        memo = {}
        res = self.dfs(num, 0, k, memo)
        return str(res)

    def dfs(self, num, i, k, memo):
        n = len(num)
        if (i, k) in memo:
            return memo[(i, k)]
        if i >= n and k <= 0:
            return 0
        if i >= n or k <= 0:
            return 10 ** 10

        remove = self.dfs(num, i + 1, k - 1, memo)
        keep = self.dfs(num, i + 1, k, memo) * 10 + int(num[i])
        memo[(i, k)] = min(remove, keep)
        print(remove, keep)
        return memo[(i, k)]




num = "1432219"
k = 3
a = SolutionTest()
print(a.removeKdigits(num, k))
