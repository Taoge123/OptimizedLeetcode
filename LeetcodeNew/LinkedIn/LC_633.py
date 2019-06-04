
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        sq = set()
        count = int(math.sqrt(c))
        # use (count + 1) because first index is 0
        for i in range(count + 1):
            sq.add(i ** 2)

        for n in sq:
            if c - n in sq:
                return True

        return False


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        maxs = 1
        while (maxs * maxs) < c:
            maxs += 1

        lo = 0
        hi = maxs
        while lo <= hi:
            if ((lo * lo) + (hi * hi)) == c:
                return True
            if ((lo * lo) + (hi * hi)) < c:
                lo += 1
            if ((lo * lo) + (hi * hi)) > c:
                hi -= 1

        # Bruthe force until maxs O(n^2)
        # for i in range(1,maxs):
        #    for j in range(1,maxs):
        #        if c == (i*i + j*j):
        #            return True

        return False






