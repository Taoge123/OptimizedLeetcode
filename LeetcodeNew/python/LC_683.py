

class Solution:
    def kEmptySlots(self, flowers, k):
        n = len(flowers)
        if n == 0 or k >= n:
            return -1

        k += 1
        size = (n + k) // k
        lows = [float('inf') for i in range(size)]
        highs = [float('-inf') for i in range(size)]

        for i in range(n):
            x = flowers[i]
            p = x // k
            if x < lows[p]:
                lows[p] = x
                if p > 0 and highs[p - 1] == x - k:
                    return i + 1

            if x > highs[p]:
                highs[p] = x
                if p < size - 1 and lows[p + 1] == x + k:
                    return i + 1

        return -1



