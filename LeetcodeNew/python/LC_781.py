
import collections


class Solution:
    def numRabbits(self, answers) -> int:
        count = [0] * 1000
        res = 0
        for num in answers:
            if (count[num] % (num + 1)) == 0:
                res += num + 1
            count[num] += 1

        return res




class Solution2:
    def numRabbits(self, answers) -> int:
        table = collections.defaultdict(int)
        for num in answers:
            table[num] += 1

        res = 0
        for num in table.keys():
            res += (table[num] + num) // (num + 1) * (num + 1)

        return res

