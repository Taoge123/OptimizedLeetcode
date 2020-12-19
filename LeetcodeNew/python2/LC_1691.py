import functools

class Solution:
    def maxHeight(self, cuboids) -> int:
        cuboids = sorted((sorted(x, reverse=True) for x in cuboids), reverse=True)
        # print(cuboids)

        @functools.lru_cache(None)
        def fn(i, h, l, w):
            """Return max heights of stacking cuboids[i:]."""
            if i == len(cuboids):
                return 0 # no cuboids left
            hi, li, wi = cuboids[i]
            if hi <= h and li <= l and wi <= w:
                return max(hi + fn( i +1, hi, li, wi), fn( i +1, h, l, w))
            else:
                return fn( i +1, h, l, w)

        return fn(0, float('inf'), float('inf'), float('inf'))




