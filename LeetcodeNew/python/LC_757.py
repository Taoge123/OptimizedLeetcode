
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda (s, e) : (s, -e))
        intervals.sort(key = lambda x : (x[1], -x[0]))

        first = -1
        second = -2
        res = 0

        for start, end in intervals:
            if start <= second:
                continue
            elif start <= first:
                res += 1
                second = first
                first = end
            else:
                res += 2
                second = end - 1
                first = end
        return res

"dcce".index()