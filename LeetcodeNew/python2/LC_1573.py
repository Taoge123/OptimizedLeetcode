"""
0101 [0000] 101 [00] 10010
"""


class Solution:
    def numWays(self, s: str) -> int:
        count = 0
        table = {}
        n = len(s)
        mod = 10 ** 9 + 7

        for i in range(n):
            if s[i] == '1':
                count += 1
                table[count] = i

        if count % 3 != 0:
            return 0

        # corner case in case all the them are 0
        if count == 0:
            return (n - 1) * (n - 2) // 2 % mod

        x = table[count // 3 + 1] - table[count // 3]
        y = table[count // 3 * 2 + 1] - table[count // 3 * 2]

        return (x * y) % mod


