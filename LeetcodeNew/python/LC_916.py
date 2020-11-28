import collections

class Solution:
    def wordSubsets(self, A, B):
        count = collections.Counter()

        for b in B:
            cb = collections.Counter(b)
            for ch, val in cb.items():
                count[ch] = max(count[ch], val)

        res = []
        for a in A:
            success = True
            ca = collections.Counter(a)
            for ch, val in count.items():
                if val > ca[ch]:
                    success = False
                    break

            if success:
                res.append(a)
        return res



