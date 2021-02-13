
class Solution:
    def intervalIntersection(self, A, B):

        res = []
        i, j = 0, 0
        if A and B:
            while i < len(A) and j < len(B):
                low = max(A[i][0], B[j][0])
                high = min(A[i][1], B[j][1])
                if low <= high:
                    res.append([low, high])
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    j += 1

        return res


# not recommended since the input is already sorted
class Solution2:
    def intervalIntersection(self, firstList, secondList):

        queue = []
        for s, e in firstList:
            queue.append([s, 1])
            queue.append([e, -1])

        for s, e in secondList:
            queue.append([s, 1])
            queue.append([e, -1])

        queue.sort(key=lambda x: (x[0], -x[1]))
        start, end = 0, 0
        count = 0
        res = []
        for time, c in queue:
            count += c
            # seeing the second starting point, then it's a starting point
            if c == 1 and count == 2:
                start = time
            # seeing the first ending point, then it's a ending point
            elif c == -1 and count == 1:
                end = time
                res.append([start, end])
        return res




