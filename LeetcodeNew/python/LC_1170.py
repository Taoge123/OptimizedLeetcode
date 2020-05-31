import bisect

class Solution:
    def numSmallerByFrequency(self, queries, words):
        # 1. Capture counts of smallest characters in each word, and sort
        # the list in ascending order.
        count = sorted([w.count(min(w)) for w in words])

        res = []
        for q in queries:
            # 2. Perform binary search of smallest characters in each query
            # against the sorted list from step#1.
            cnt = q.count(min(q))
            idx = bisect.bisect(count, cnt)
            res.append(len(words) - idx)
        return res


