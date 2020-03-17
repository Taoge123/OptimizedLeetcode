
class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        parents = {region[i] : region[0] for region in regions for i in range(1, len(region))}

        regionOne = {region1}
        while region1 in parents:
            region1 = parents[region1]
            regionOne.add(region1)
        while region2 not in regionOne:
            region2 = parents[region2]
        return region2





