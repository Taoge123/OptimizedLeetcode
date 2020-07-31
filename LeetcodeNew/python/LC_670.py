"""

99 2 34 4 3
   -    -
选后面的4

"""

class SolutionTony:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        t = s
        t = sorted(t)[::-1]
        i = 0
        while i < len(s) and s[i]==t[i]:
            i += 1
        if i == len(s):
            return num

        pos = 0
        for j in range(i+1, len(s)):
            if s[j] == t[i]:
                pos = j
        s[i], s[pos] = s[pos], s[i]
        return s



class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        res = num[:]
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                if num > res:
                    res = num[:]
                num[i], num[j] = num[j], num[i]

        return int("".join(res))


"""
We can also get an O(N) solution. At each digit, if there is a larger digit that occurs later, 
we want the swap it with the largest such digit that occurs the latest.
"""


class Solution2:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        table = {int(x): i for i, x in enumerate(s)}
        for i, x in enumerate(s):
            for digit in range(9, int(x), -1):
                if table.get(digit, 0) > i:
                    s[i], s[table[digit]] = s[table[digit]], s[i]
                    return int("".join(s))
        return num




a = SolutionTony()
print(a.maximumSwap(2736))

