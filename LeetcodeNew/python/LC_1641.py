"""
      a e i o u
1 ->  1 1 1 1 1
2 ->  1 2 3 4 5
3 ->          5+4+3+2+1
            4+3+2+1
          3+2+1
        2+1

a 5 aa ae ai ao au -> 15
e 4 ee ei eo eu    ->
i 3 ii io iu
o 2 oo ou
u 1 uu


a e i o u
1 2 3 4 5

3 ->

dp[1] = 5
dp[2] = 5 + 4 + 3 + 2 + 1 = 15
dp[3] = 15 * a + 14 * e +

"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 15

        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = a, a + e, a + e + i, a + e + i + o, a + e + i + o + u
        return a + e + i + o + u






