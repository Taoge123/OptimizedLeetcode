
def __init__(self, w):
    self.w = list(itertools.accumulate(w))

def pickIndex(self):
    return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))





class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.n = len(w)
        self.s = sum(self.w)
        for i in range(1,self.n):
            w[i] += w[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(1,self.s)
        l,r = 0, self.n-1
        while l<r:
            mid = (l+r)//2
            if seed <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l


class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)): w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        x = random.randint(1, self.w[-1])
        return bisect.bisect_left(self.w, x)


