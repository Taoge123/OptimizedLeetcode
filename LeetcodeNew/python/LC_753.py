
"""
youtube.com/watch?v=kRdlLahVZDc



题目大意
题目描述是一个智能门锁，这个门锁只识别最近的n个字符，只要有连续的n个字符输入对了，前面无论输入什么都无所谓。那么，让我们求一个最短的万能钥匙串，能破解这个门锁的所有可能密码。

解题方法
显而易见，如果要这个万能钥匙串足够短，那么可以预料的是，每个密码都复用前面的密码，那么最优情况下就是，每个密码复用前面的n - 1位密码。
额，这个数学问题叫做De Bruijin sequence，已经证明了每个可能的密码都可以在一个万能钥匙串中出现并且只出现一次。
（Leetcode出这样的题也是让人没辙）

n位的密码锁，每个位置可以有k个数，所以总的可能性是k ^ n个。然后我们从前n位是0的状态开始，每次在后面添加一个新的字符，
同时使用set保存这个出现过的新密码。当新密码的种类数等于 k ^ n时，搜索截止。

数学上已经郑明，这样的串是最短的串，而且，能解决所有可能的密码数。

python由于是值传递，可以通过给函数传list的方式，直接修改list内会导致外边的List也变化，但是传string不行。
string是不可变的对象，函数内部修改string不会影响到外边。因此，如果需要动态生成字符串，可以把string变成list当做函数的参数。

时间复杂度是O(Nlog(N))，空间复杂度是O(N)。
"""

"""
De Bruijin Sequence -> n^k + (n-1)
Hamilton Cycle - each vertex visited once
Euler Cycle - each edge visited once

[XXXXXXX] [X]

"""


class Solution:
    def crackSafe(self, n, k):
        res = ["0"] * n
        total = k ** n
        visited = set()
        visited.add("".join(res))
        if self.dfs(total, n, k, visited, res):
            return "".join(res)
        return ""

    def dfs(self, total, n, k, visited, res):
        if len(visited) == total:
            return True
        node = "".join(res[len(res) - n + 1:])
        for i in range(k):
            node = node + str(i)
            if node in visited:
                continue

            res.append(str(i))
            visited.add(node)
            if self.dfs(total, n, k, visited, res):
                return True
            res.pop()
            visited.remove(node)

            node = node[:-1]



