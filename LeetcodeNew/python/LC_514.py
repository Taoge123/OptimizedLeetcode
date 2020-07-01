"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom
Trail Ring",
and use the dial to spell a specific keyword in order to open the door.
Given a string ring, which represents the code engraved on the outer ring and another string key,
which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all
the characters in the keyword.
Initially, the first character of the ring is aligned at 12:00 direction.
You need to spell all the characters in the string key one by one by rotating the ring clockwise
or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center
button.
At the stage of rotating the ring to spell the key character key[i]:
You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the
rotation is to align one of the string ring's characters at the 12:00 direction,
where this character must equal to the character key[i].
If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell,
which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage),
otherwise, you've finished all the spelling.
Example:
Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become
"ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Note:
Length of both ring and key will be in range 1 to 100.
There are only lowercase letters in both strings and might be some duplcate characters in both strings.
It's guaranteed that string key could always be spelled by rotating the string ring.
"""

import collections


class SolutionTLE:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        dp = [[0 for i in range(n)] for j in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n):
                dp[i][j] = float('inf')
                for k in range(n):
                    if ring[k] == key[i]:
                        diff = abs(j - k)
                        step = min(diff, n - diff)
                        dp[i][j] = min(dp[i][j], step + dp[i + 1][k])

        return dp[0][0] + m


"""
dp[i][cur_pos] : at the i-round, we are going to move the letter at ring[pos] to 12 o'clock
                min number of steps in order to spell all the characters in the keyword[0:i]

dp[i][pos] => dp[i-1][prev] + dis(prev, pos) for prev = ......

"""


class SolutionWidsom:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m, n = len(ring), len(key)
        dp = [[float('inf') for i in range(m)] for j in range(n)]
        table = collections.defaultdict(list)
        for i, char in enumerate(ring):
            table[char].append(i)

        for i in range(n):
            if i == 0:
                for pos in table[key[i]]:
                    dp[i][pos] = min(pos, abs(m - pos))
            elif i >= 1:
                for cur in table[key[i]]:
                    for prev in table[key[i - 1]]:
                        dp[i][cur] = min(dp[i][cur], dp[i - 1][prev] + min(abs(cur - prev), m - abs(cur - prev)))

        res = float('inf')
        for pos in table[key[n - 1]]:
            res = min(res, dp[n - 1][pos])

        return res + n


class Solution1:
    def findRotateSteps(self, ring: str, key: str) -> int:
        table = collections.defaultdict(list)
        for i, val in enumerate(ring):
            table[val].append(i)

        n = len(ring)
        init = {0: 0}

        for char in key:
            dp = {}
            for i in table[char]:
                dp[i] = float('inf')
                for j in init:
                    dp[i] = min(dp[i], init[j] + min(abs(i - j), n - abs(i - j)))
            init = dp

        return min(dp.values()) + len(key)


class Solution2:
    def findRotateSteps(self, ring, key):
        table = collections.defaultdict(list)
        pre = key[0]
        dp = [0] * len(ring)
        n = len(ring)
        for i, char in enumerate(ring):
            table[char].append(i)
        for i in table[key[0]]:
            dp[i] = min(i, n - i) + 1
        for char in key[1:]:
            for i in table[char]:
                dp[i] = min(dp[j] + min(abs(i - j), n - abs(i - j)) for j in table[pre]) + 1
            pre = char
        return min(dp[i] for i in table[key[-1]])


class Solution3Fast:
    def findRotateSteps(self, ring, key):
        cache = {}
        table = collections.defaultdict(list)
        for i, char in enumerate(ring):
            table[char].append(i)
        n = len(ring)
        return self.dfs(key, 0, table, n, cache)

    def dfs(self, key, pos, table, n, cache):
        if (pos, key) in cache:
            return cache[pos, key]
        if not key:
            return 0
        res = float("inf")
        toChar = key[0]
        for i in table[toChar]:
            diff = min(n - abs(pos - i), abs(pos - i))
            res = min(res, diff + 1 + self.dfs(key[1:], i, table, n, cache))
        cache[pos, key] = res
        return res


class Solution4:
    def findRotateSteps(self, ring, key):
        memo = {}
        n = len(ring)
        return self.dfs(ring, key, 0, 0, n, memo)

    def dfs(self, ring, key, pos, idx, n, memo):
        if (pos, idx) in memo:
            return memo[(pos, idx)]
        if pos >= len(key):
            return 0
        res = float('inf')
        for i in range(n):
            nxt = (i + idx) % n
            if ring[nxt] != key[pos]:
                continue
            diff = min(i, n - i)
            res = min(res, diff + 1 + self.dfs(ring, key, pos + 1, nxt, n, memo))
        memo[(pos, idx)] = res
        return res



ring = "godding"
key = "gd"

a = Solution2()
print(a.findRotateSteps(ring, key))
