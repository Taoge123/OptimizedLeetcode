
class Solution:
    def flipgame(self, fronts, backs) -> int:
        cards = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cards.add(fronts[i])

        res = float('inf')
        for i in range(len(fronts)):
            if backs[i] not in cards:
                res = min(res, backs[i])

            if fronts[i] not in cards:
                res = min(res, fronts[i])

        return res if res != float('inf') else 0


