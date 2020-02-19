
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        res = num[:]
        for i in range(len(num)):
            for j in range(i +1, len(num)):
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
        temp = list(str(num))
        table = {int(x): i for i, x in enumerate(temp)}
        for i, x in enumerate(temp):
            for digit in range(9, int(x), -1):
                if table.get(digit, 0) > i:
                    temp[i], temp[table[digit]] = temp[table[digit]], temp[i]
                    return int("".join(temp))
        return num






