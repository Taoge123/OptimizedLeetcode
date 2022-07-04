
"""
rand()%N
M
rand()%M -- U[0, M-1]

1 2 (3) 4 5 6 7 (8) (9)
1 2 4 5 6 7 (3) (8) (9)


"""


"""
https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping


1234567  234
    i
j
table[]
table = {2 : 5,
         3 : 6,
         4 : 7,
  }
self.length = 4

"""

import random


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()


class Solution:
    def __init__(self, n: int, blacklist):
        m = len(blacklist)
        self.upper = n - m  # 可选的数一共n-m个
        self.map = dict()  # 转换的哈希表，key：黑名单，val：转换的白名单
        i = self.upper  # 下一个可取的值
        blacklist = set(blacklist)
        for node in blacklist:  # 遍历黑名单
            if node < self.upper:  # 如果黑名单元素在[0,n-m),那么需要被转换
                while i in blacklist:
                    i += 1
                self.map[node] = i
                i += 1

    def pick(self) -> int:
        num = random.randint(0, self.upper - 1)
        return self.map.get(num, num)




class Solution2:
    def __init__(self, N: int, blacklist):
        blacklist = sorted(blacklist)
        self.blacklist = set(blacklist)
        self.table = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.blacklist:
                self.table[blacklist[j]] = i
                j += 1

    def pick(self) -> int:
        i = random.randint(0, self.length - 1)
        return self.table[i] if i in self.table else i



class SolutionTLE:
    def __init__(self, n: int, blacklist):
        self.n = n
        self.block = set(blacklist)

    def pick(self) -> int:
        while True:
            i = random.randint(0, self.n - 1)
            if i not in self.block:
                return i


