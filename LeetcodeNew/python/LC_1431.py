
class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):
        maxi = max(candies)

        res = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                res.append(True)
            else:
                res.append(False)
        return res


