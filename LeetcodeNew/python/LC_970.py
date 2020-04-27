
class Solution:
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        # 2**18 > bound
        for i in range(25):
            for j in range(25):
                v = x** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)


class SolutionLee:
    def powerfulIntegers(self, x, y, bound):
        xs = {x**i for i in range(20) if x**i < bound}
        ys = {y**i for i in range(20) if y**i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})



