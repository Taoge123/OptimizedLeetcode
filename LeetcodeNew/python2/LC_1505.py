
"""
XXXXX 1 XXXXX
next[0] = -1
next[1] = 5
next[2] = ...


Y X XXXX j XX (Y) XX
  i

 next[j] + offset[j] - i


"""

import collections


class Fenwick:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def query(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans += self.sums[i]
            i -= i & -i
        return ans

    def update(self, i, delta):
        i += 1
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        visited = [False] * n
        pos = [collections.deque() for _ in range(10)]
        for i, char in enumerate(num):
            pos[ord(char) - ord("0")].append(i)
        tree = Fenwick(n)
        res = []
        while k > 0 and len(res) < n:
            for digit in range(10):
                if not pos[digit]:
                    continue
                i = pos[digit][0]
                cost = i - tree.query(i - 1)
                if cost > k:
                    continue
                k -= cost
                res.append(chr(digit + ord("0")))
                tree.update(i, 1)
                visited[i] = True
                pos[digit].popleft()
                break
        for i in range(n):
            if not visited[i]:
                res.append(num[i])
        return "".join(res)






class Solution2:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        mp = collections.defaultdict(deque)
        for i,v in enumerate(num):
            mp[v].append(i)
        res = ""
        def lowbit(x):
            return x & (-x)
        def query(x):
            sums = 0
            while x:
                sums += arr[x]
                x -= lowbit(x)
            return sums
        def update(x,delta):
            while x <= n:
                arr[x] += delta
                x += lowbit(x)

        arr = [0]*(n+1)
        for i in range(n):
            update(i+1,1)

        for i in range(n):
            for v in "0123456789":
                if mp[v]:
                    idx = mp[v][0]
                    cnt = query(idx)
                    if cnt > k: continue
                    mp[v].popleft()
                    k -= cnt
                    res += v
                    update(idx+1,-1)
                    break
        return res

