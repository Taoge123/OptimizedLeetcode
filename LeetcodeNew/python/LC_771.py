
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        Set = set()

        for j in J:
            Set.add(j)

        for s in S:
            if s in Set:
                res += 1
        return res


