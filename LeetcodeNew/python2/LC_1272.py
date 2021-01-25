"""
-----------
   -----------
     -------------
                    ------
                            -----
                              --------

"""

class Solution:
    def removeInterval(self, intervals, toBeRemoved):

        res = []
        for start, end in intervals:
            if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                res.append([start, end])
                continue

            # left side have space
            if start < toBeRemoved[0]:
                res.append([start, toBeRemoved[0]])

            # right side have space
            if end > toBeRemoved[1]:
                res.append([toBeRemoved[1], end])

        return res



