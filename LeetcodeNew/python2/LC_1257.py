
class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            for i in range(1, len(region)):
                parent[region[i]] = region[0]


        history = set([region1])
        while region1 in parent:
            region1 = parent[region1]
            history.add(region1)

        while region2 not in history:
            region2 = parent[region2]

        return region2


