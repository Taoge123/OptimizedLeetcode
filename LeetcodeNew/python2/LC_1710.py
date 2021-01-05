
class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key = lambda x : -x[1])
        res = 0

        for num, units in boxTypes:
            count = min(truckSize, num)
            res += count * units
            truckSize -= count
            if truckSize == 0:
                break
        return res


